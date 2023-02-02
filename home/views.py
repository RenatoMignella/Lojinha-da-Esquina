from django.shortcuts import render

# Create your views here.


def index(request):
    """ A view to retur index"""

    return render(request, 'home/index.html')
