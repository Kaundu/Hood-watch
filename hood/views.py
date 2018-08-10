from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import *
from .forms import  ProfileForm, NeighborhoodForm,BusinessForm,PostForm
from hood.models import  Profile,Neighborhood,Business

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    hoods = Neighborhood.objects.all()
    # users = User.objects.get(id=user_id)
    return render(request, 'index.html', locals())

# def neighborhood(request):



@login_required(login_url='/accounts/login')
def profile(request, user_id):
	users = User.objects.get(id = user_id)
	profile = Profile.objects.get(user= users)
	print(profile)
	return render(request, 'profile.html', locals())
