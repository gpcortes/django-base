from django.shortcuts import render
from django.contrib import messages


def get_header(request):
    template_name = 'header.html'
    context = {
        'content': '',
    }
    return render(request=request, template_name=template_name, context=context, content_type="text/plain")


def get_nav(request):
    template_name = 'nav.html'
    context = {
        'content': '',
    }
    return render(request=request, template_name=template_name, context=context, content_type="text/plain")


def get_footer(request):
    template_name = 'footer.html'
    context = {
        'content': '',
    }
    return render(request=request, template_name=template_name, context=context, content_type="text/plain")


def get_home(request):
    template_name = 'index.html'
    content = {}
    header = get_header(request).content.decode("utf-8")
    nav = get_nav(request).content.decode("utf-8")
    footer = get_footer(request).content.decode("utf-8")
    context = {
        'content': content,
        'header': header,
        'nav': nav,
        'footer': footer,
    }
    messages.success(request, f'Olá {request.user.first_name}, seja bem vindo(a)!')
    return render(request=request, template_name=template_name, context=context)
