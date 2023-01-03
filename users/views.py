from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login, logout
from .forms import UseRegistrationForm
from django.contrib import messages

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