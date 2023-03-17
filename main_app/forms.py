from django.forms import ModelForm
from .models import Post

class WorkForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'rate', 'status']
        # fields.status = 'n'