from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from captcha import fields
from captcha import widgets
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.forms import PasswordResetForm

class PasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(PasswordResetForm, self).__init__(*args, **kwargs)
            # captcha = ReCaptchaField(widget=R())
    captcha = fields.ReCaptchaField(
    widget=widgets.ReCaptchaV2Checkbox(
        attrs={
           
        }
    )
)
        
class UseRegistrationForm(UserCreationForm):
    email = forms.EmailField(help_text='A valid Email Please!',required=True)
    
    class Meta:
        model = get_user_model()
        fields =['username','email','password1','password2']
        
        
    def save(self,commit=True):
        user = super(UseRegistrationForm,self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user    
class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Username or Email'}),
        label="Username or Email*")

    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password'}))           
    
    
    # captcha = ReCaptchaField(widget=R())
    captcha = fields.ReCaptchaField(
    widget=widgets.ReCaptchaV2Checkbox(
        attrs={
           
        }
    )
)
class UseUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = get_user_model()
        fields = ['username','email','description','image']
        
        

class SetPasswordForm(SetPasswordForm):
    class Meta:
        model = get_user_model()
        fields = ['new_password1', 'new_password2']       