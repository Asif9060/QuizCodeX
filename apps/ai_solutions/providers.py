"""AI provider implementations used by the services layer.

Switch the active provider by setting AI_ACTIVE_PROVIDER in .env:
  AI_ACTIVE_PROVIDER=ollama          # default — local Ollama server
  AI_ACTIVE_PROVIDER=openai          # OpenAI Chat Completions
  AI_ACTIVE_PROVIDER=gemini          # Google Gemini
  AI_ACTIVE_PROVIDER=anthropic       # Anthropic Claude

Each provider reads its config (base_url / api_key / model) from
settings.AI_PROVIDERS[name] so you can change models without touching code.
"""
from __future__ import annotations

import abc
import json
import urllib.request
from typing import Tuple

from django.conf import settings


class AIProvider(abc.ABC):
    """Base class.  Returns (text, prompt_tokens, completion_tokens)."""

    @abc.abstractmethod
    def generate(self, prompt: str) -> Tuple[str, int, int]:
        ...


class OllamaProvider(AIProvider):
    """Local Ollama server — no API key required."""

    def generate(self, prompt: str) -> Tuple[str, int, int]:
        cfg = settings.AI_PROVIDERS["ollama"]
        payload = json.dumps({
            "model": cfg["model"],
            "prompt": prompt,
            "stream": False,
        }).encode()
        req = urllib.request.Request(
            f"{cfg['base_url'].rstrip('/')}/api/generate",
            data=payload,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        # Large models (480B) can take several minutes — generous timeout
        with urllib.request.urlopen(req, timeout=300) as resp:
            data = json.loads(resp.read())
        return (
            data.get("response", "").strip(),
            data.get("prompt_eval_count", 0),
            data.get("eval_count", 0),
        )


class OpenAIProvider(AIProvider):
    """OpenAI Chat Completions API (gpt-4o, gpt-4-turbo, etc.)."""

    def generate(self, prompt: str) -> Tuple[str, int, int]:
        cfg = settings.AI_PROVIDERS["openai"]
        payload = json.dumps({
            "model": cfg["model"],
            "messages": [{"role": "user", "content": prompt}],
        }).encode()
        req = urllib.request.Request(
            "https://api.openai.com/v1/chat/completions",
            data=payload,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {cfg['api_key']}",
            },
            method="POST",
        )
        with urllib.request.urlopen(req, timeout=60) as resp:
            data = json.loads(resp.read())
        usage = data.get("usage", {})
        return (
            data["choices"][0]["message"]["content"].strip(),
            usage.get("prompt_tokens", 0),
            usage.get("completion_tokens", 0),
        )


class GeminiProvider(AIProvider):
    """Google Gemini generateContent API."""

    def generate(self, prompt: str) -> Tuple[str, int, int]:
        cfg = settings.AI_PROVIDERS["gemini"]
        payload = json.dumps({
            "contents": [{"parts": [{"text": prompt}]}],
        }).encode()
        url = (
            "https://generativelanguage.googleapis.com/v1beta/models/"
            f"{cfg['model']}:generateContent?key={cfg['api_key']}"
        )
        req = urllib.request.Request(
            url,
            data=payload,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        with urllib.request.urlopen(req, timeout=60) as resp:
            data = json.loads(resp.read())
        text = data["candidates"][0]["content"]["parts"][0]["text"]
        usage = data.get("usageMetadata", {})
        return (
            text.strip(),
            usage.get("promptTokenCount", 0),
            usage.get("candidatesTokenCount", 0),
        )


class AnthropicProvider(AIProvider):
    """Anthropic Messages API (claude-3-5-sonnet, etc.)."""

    def generate(self, prompt: str) -> Tuple[str, int, int]:
        cfg = settings.AI_PROVIDERS["anthropic"]
        payload = json.dumps({
            "model": cfg["model"],
            "max_tokens": 1024,
            "messages": [{"role": "user", "content": prompt}],
        }).encode()
        req = urllib.request.Request(
            "https://api.anthropic.com/v1/messages",
            data=payload,
            headers={
                "Content-Type": "application/json",
                "x-api-key": cfg["api_key"],
                "anthropic-version": "2023-06-01",
            },
            method="POST",
        )
        with urllib.request.urlopen(req, timeout=60) as resp:
            data = json.loads(resp.read())
        usage = data.get("usage", {})
        return (
            data["content"][0]["text"].strip(),
            usage.get("input_tokens", 0),
            usage.get("output_tokens", 0),
        )


_REGISTRY: dict[str, type[AIProvider]] = {
    "ollama": OllamaProvider,
    "openai": OpenAIProvider,
    "gemini": GeminiProvider,
    "anthropic": AnthropicProvider,
}


def get_active_provider() -> AIProvider:
    """Return an instance of whichever provider settings.AI_ACTIVE_PROVIDER names."""
    name = getattr(settings, "AI_ACTIVE_PROVIDER", "ollama")
    cls = _REGISTRY.get(name)
    if not cls:
        raise ValueError(
            f"Unknown AI provider '{name}'. Valid options: {list(_REGISTRY)}"
        )
    return cls()
