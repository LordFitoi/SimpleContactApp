from allauth.account.adapter import DefaultAccountAdapter
from django.conf import settings
from django.http import HttpRequest

class AccountAdapter(DefaultAccountAdapter):
    def get_login_redirect_url(self, request: HttpRequest):
        path = "/profile/{username}/"
        return path.format(username=request.user.username)
