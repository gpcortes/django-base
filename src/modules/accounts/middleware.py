from django.shortcuts import redirect
from django.conf import settings
from django.utils.deprecation import MiddlewareMixin
from django.urls import reverse_lazy


class ProcessRequestMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, *view_args, **view_kwargs):
        user = request.user
        path = request.path_info.lstrip('/')
        modules = path.split('/')
        if modules[0] not in settings.PUBLIC_URL_PATHS and not user.is_authenticated:
            return redirect(reverse_lazy('SignIn') + f'?next=/{path}')