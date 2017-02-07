from django.http import HttpResponse

# Create your views here.


def index(request):
    """
    Serve an http response
    :param request: HttpResponse
    :return: HTML response
    """
    return HttpResponse("<h2>Hey!</h2>")
