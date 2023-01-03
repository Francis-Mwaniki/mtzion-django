from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login, logout, authenticate
from .forms import UseRegistrationForm, UserLoginForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from  .decorators import user_not_authenticated


@user_not_authenticated
def register(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method=='POST':
        form = UseRegistrationForm(request.POST)
        if form.is_valid():
            user= form.save()
            login(request,user)
            messages.success(request, f"New account created: {user.username}")
            return redirect('/')
        else:
            for error in list(form.errors.values()):
                 messages.error(request,error)
    else:
         form = UseRegistrationForm()  
    return render(
        request = request,
        template_name = "users/register.html",
        context={"form":form}
    )              
@login_required
def custom_logout(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("home")    

@user_not_authenticated
def custom_login(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = UserLoginForm(request=request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                messages.success(request, f"Hello {user.username} You have been logged in")
                return redirect('home')

        else:
            for key, error in list(form.errors.items()):
                if key == 'captcha' and error[0] == 'This field is required.':
                   messages.error(request, "You must pass the reCAPTCHA test")
                   continue
                messages.error(request, error) 

    form = UserLoginForm() 
    
    return render(
        request=request,
        template_name="users/login.html", 
        context={'form': form}
        )