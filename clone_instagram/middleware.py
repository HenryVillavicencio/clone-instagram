"""clone-instagram middleware ctalog """


# Django

from django.shortcuts import redirect
from django.urls import reverse


class ProfileCompletionMiddleware:
    """ProfileCompletionMiddleware.

    Ensure every user that is interacting with the plataform 
    haver their picture profile and biography.
    """

    def __init__(self, get_response):
        """Middleware initialization"""
        self.get_response = get_response

    def __call__(self, request):
        """Code to be executed for each request before the viw is called. """
        if not request.user.is_anonymous:
            if not request.user.is_staff:
                profile = request.user.profile
                if not profile.picture or not profile.website:
                    if request.path not in[reverse('users:update'), reverse('users:logout')]:
                        return redirect('users:update')
        response = self.get_response(request)
        return response
