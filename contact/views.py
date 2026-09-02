from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout



def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user= form.save()
            login(request,user)
            return redirect('login')
        else:
            print('Errors:', form.errors)
        
    else:
        form= UserCreationForm()
    return render(request, 'contact/registered.html', {'form':form})


def login_view(request):
    if request.method =='POST':
        form= AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user= form.get_user()
            login(request, user)
            return redirect('/blog/blog/')
        else:
            print('Errors:', form.errors)
    else:
        form= AuthenticationForm()
    return render(request, 'contact/login.html', {'form': form})


def dashboard_view(request):
    pass

def logout_view(request):
    pass

