from django.shortcuts import render
from django.http import HttpResponse
from proTwo_app.models import User
# Create your views here.

def index(request):
    users = User.objects.order_by('email')
    data = {'access':users}
    return render(request,'proTow_app/index.html',context=data)
