import re
from django.template import Context, Template
from django.http import HttpResponse, HttpResponseServerError
from django.core.exceptions import ValidationError
from django.conf import settings
import tidy
from django_minify_html.middleware import MinifyHtmlMiddleware
from django.http import HttpResponse
from django.contrib import messages
from django.core.handlers.base import BaseHandler
import traceback

class ProjectMinifyHtmlMiddleware(MinifyHtmlMiddleware):
    minify_args = MinifyHtmlMiddleware.minify_args | {
        "keep_comments": False,
    }


class ExceptionsMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

    # def process_exception(self, request, exception):
    #     if not settings.DEBUG:
    #         if exception:
    #             # Format your message here
    #             message = "**{url}**\n\n{error}\n\n````{tb}````".format(
    #                 url=request.build_absolute_uri(),
    #                 error=repr(exception),
    #                 tb=traceback.format_exc()
    #             )
    #             # Do now whatever with this message
    #             # e.g. requests.post(<slack channel/teams channel>, data=message)
                
    #         return HttpResponse("Error processing the request.", status=500)
        
        