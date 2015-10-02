from django.contrib.auth.models import User
from django import forms
class SignUpForm(forms.Form):
    #we are taking email as unique username
    username = forms.CharField()
    password = forms.CharField(label=(u'Password'), widget=forms.PasswordInput(render_value=False))
    password_again = forms.CharField(label=(u'Verify Password'), widget=forms.PasswordInput(render_value=False))
    salary=forms.CharField()
    profession=forms.CharField()
    phone=forms.CharField()
    city=forms.CharField()
    state=forms.CharField()

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            User.objects.get(username =  username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError("This email is already registered")

class SignInForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(label=(u'Password'), widget=forms.PasswordInput(render_value=False))

class ForgetPasswordForm(forms.Form):
    email  = forms.CharField(required  = True)

class NewPasswordForm(forms.Form):
    user_id = forms.CharField()
    new_password = forms.CharField(label= u'New password', widget=forms.PasswordInput, required = True)
    new_password_again = forms.CharField(label = u'Verify password', widget = forms.PasswordInput, required = True)
