from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login, logout, authenticate
from .forms import UseRegistrationForm, UserLoginForm, UseUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from  .decorators import user_not_authenticated
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage


from .tokens import account_activation_token

def activateEmail(request, user, to_email):
    mail_subject = 'Activate your user account.'
    message = render_to_string('template_activate_account.html', {
        'user': user.username,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        'protocol': 'https' if request.is_secure() else 'http'
    })
    email = EmailMessage(mail_subject, message, to=[to_email])
    if email.send():
        messages.success(request, f'Dear <b>{user}</b>, please go to you email <b>{to_email}</b> inbox and click on \
            received activation link to confirm and complete the registration. <b>Note:</b> Check your spam folder.')
    else:
        messages.error(request, f'Problem sending confirmation email to {to_email}, check if you typed it correctly.')
@user_not_authenticated
def register(request):
    if request.method == "POST":
        form = UseRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            activateEmail(request, user, form.cleaned_data.get('email'))
            return redirect('homepage')

        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

    else:
        form = UseRegistrationForm()

    return render(
        request=request,
        template_name="users/register.html",
        context={"form": form}
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
def profile(request,username):
    if request.method=='POST':
        user = request.user
        form = UseUpdateForm(request.POST,request.FILES,instance=user)
        if form.is_valid():
            user_form = form.save()
            
            messages.success(request,f'{user_form} Your profiles has been updated')
            return redirect('profile',user_form.username)
        for error in list(form.errors.values()):
               messages.error(request,error)
    user =get_user_model().objects.filter(username=username).first()
    if user:
        form = UseUpdateForm(instance=user)
        form.fields['description'].widget.attrs={'row':2}
        return render(request,'users/profile.html',context={'form':form})
    return redirect('home')           