from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from user_app.forms import UserForm

# Create your views here.

def main(request):
    return render(request, 'user_app/main.html')

def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        #profile_form = ProfileForm(data=request.POST)

        if user_form.is_valid():

            user = user_form.save()
            # hashing the password
            user.set_password(user.password)
            user.save()
            registered = True

        else:
            print(user_form.errors)

    else:
        user_form = UserForm()
        #profile_form = ProfileForm()

    context = {'user_form':user_form, 'registered':registered}
    return render(request, 'user_app/registration.html', context=context)
    

def user_login(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request=request, user=user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('Account not active')
            
        else:
            print('Someone tried to login and failed')
            print("Username: {} and password: {}".format(username, password))
            return HttpResponse('Invalid login and/or password')
    
    else:
        return render(request, 'user_app/login.html', {})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))