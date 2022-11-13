from django.contrib.auth import get_user_model
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
class UserAdminCreationForm(forms.ModelForm):
    password1=forms.CharField(label='Password',widget=forms.PasswordInput)
    password2=forms.CharField(label='confirm Password',widget=forms.PasswordInput)

    class Meta:
        model=get_user_model()
        fields=['email']
        
    def clean_password2(self):
        p1=self.cleaned_data['password1']
        p2=self.cleaned_data['password2']
        if p1 and p2 and p1 != p2:
            return forms.ValidationError('passwords not matched')
        return p2
    def save(self,commit=True):
        user=super(UserAdminCreationForm,self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user    

class UserAdminChangeForm(forms.ModelForm):
    password=ReadOnlyPasswordHashField
    class Meta:
        model=get_user_model()
        fields=['email','password','active','staff','admin']

    def clean_password(self):
        return self.initial['password']

class UserForm(forms.ModelForm):
    class Meta:
        model=get_user_model()
        fields=['username','email','password']