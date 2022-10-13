
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from accounts.models import Users

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]

from django.contrib.auth.forms import UserChangeForm

class CustomUserChangeForm(UserChangeForm):
    
    class Meta:
        model = get_user_model()
        fields = ['email', 'first_name', 'last_name']
        

        # fields = [
            
        #     'email', 
        #     'first_name',
        #     'last_name',
            
        # ]
        