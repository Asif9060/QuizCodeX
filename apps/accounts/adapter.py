"""Custom allauth adapter — controls signup/login behaviour."""
from allauth.account.adapter import DefaultAccountAdapter
from django.conf import settings


class AccountAdapter(DefaultAccountAdapter):
    """
    Override allauth defaults:
    - Use our custom login/register URLs rather than allauth's own templates
    - Redirect after login/logout to the configured settings values
    """

    def get_login_redirect_url(self, request):
        return settings.LOGIN_REDIRECT_URL

    def get_logout_redirect_url(self, request):
        return settings.LOGOUT_REDIRECT_URL

    def is_open_for_signup(self, request):
        """Allow all registrations for now; hook here to add invite-only logic."""
        return True
