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

@login_required(login_url='/accounts/login')
def neighborhood(request,neighborhood_id):
    businesses = Business.objects.all()
    posts = Post.objects.all()
    return render(request, 'neighborhood.html', locals())

def business(request, business_id):
    businesses = Business.objects.all()
    return render(request, 'business.html' , locals())

@login_required(login_url='/accounts/login')
def updateprofile(request):
	if request.method == 'POST':
		form = ProfileForm(request.POST,request.FILES, instance=request.user.profile)
		if form.is_valid():
			form.save()
			return redirect('index')

	else:
			form = ProfileForm()
	return render(request, 'updateprofile.html',{"form":form })

def join_neighborhood(request,n_id):
    neighborhood = Neighborhood.objects.get(pk=n_id)
    request.user.profile.neighbor_hood=neighborhood
    request.user.profile.save()
    return redirect('/neighborhood/'+f'{n_id}')


def new_neighborhood(request):
    current_user = request.user

    if request.method == 'POST':
        form = NeighborhoodForm(request.POST, request.FILES)
        if form.is_valid():
            neighborhood = form.save(commit=False)
            neighborhood.user = current_user
            neighborhood.save()
            return redirect('index')
    else:
        form = NeighborhoodForm()
    return render(request, 'new_neighborhood.html', {"form": form})

def new_business(request):
    current_user = request.user

    if request.method == 'POST':
        form = BusinessForm(request.POST, request.FILES)
        if form.is_valid():
            business = form.save(commit=False)
            business.user = current_user
            business.save()
            return redirect('index')

    else:
        form = BusinessForm()
    return render(request, 'new_business.html', {"form": form})


def new_post(request):
    current_user = request.user

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
            return redirect('index')
    else:
        form = PostForm()
    return render(request, 'new_post.html', {"form": form})
