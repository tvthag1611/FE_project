from django.shortcuts import render

# Create your views here.
def index_view(request):
    return render(request, "login/index.html")

def index_view_register(request):

    return render(request, "register/register.html")

