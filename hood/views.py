from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from hood.models import  Profile,Neighborhood,Business

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    return render(request, 'index.html', locals())    hoods = Neighborhood.objects.all()
    # users = User.objects.get(id=user_id)
    return render(request, 'index.html', locals())

# def neighborhood(request):

