from django.shortcuts import render

# Create your views here.

def index_choose_member(request):
    return render(request, "choose_member.html")