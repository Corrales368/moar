from django.shortcuts import render


def handler404(request, *args, **argv):
    response = render(request, 'shared/error/404.html')
    return response


def handler500(request, *args, **argv):
    response = render(request, 'shared/error/500.html')
    return response