from django.forms import ModelForm
from .models import Post1,Post2

class Request(ModelForm):
    class Meta:
        model = Post1
        fields = '__all__'

class Supply(ModelForm):
    class Meta:
        model = Post2
        fields = '__all__'

