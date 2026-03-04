"""
Core signals — event bus between apps.
Use Django signals to decouple apps instead of direct imports.

Future: When quiz_completed fires, leaderboard, contests, and
ai_solutions apps hook in here without touching quiz logic.
"""
from django.dispatch import Signal

# Custom signals
quiz_completed = Signal()  # sender=UserResult instance
# Usage: quiz_completed.send(sender=result, user=result.user, quiz=result.quiz)
