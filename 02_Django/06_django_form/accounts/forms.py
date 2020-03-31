from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model 

class CustomUserChangeForm(UserChangeForm): # UserChangForm을 상속받아 커스텀하는 클래스
    class Meta:
        model = get_user_model()
        fields= ('email', 'first_name', 'last_name', )

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'password1', 'password2', 'email', )
        