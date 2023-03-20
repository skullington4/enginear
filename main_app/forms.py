from django.forms import ModelForm
from .models import Posts

class WorkForm(ModelForm):
    class Meta:
        model = Posts
        fields = ['title', 'description', 'rate',]
        # fields.status = 'n'