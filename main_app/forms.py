from django.forms import ModelForm
from .models import Post, Comment

class WorkForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'rate', 'status', 'is_business']
        
class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['description']