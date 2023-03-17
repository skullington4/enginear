from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User
# Create your models here.

STATUS = (
    ('N', 'New'),
    ('I', 'In Progress'),
    ('C', 'Complete')
)

class Posts(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField(max_length=250)
    rate = models.IntegerField()
    status = models.CharField(
        max_length=1,
        choices=STATUS,
        default=STATUS[0][0]
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'finch_id': self.id})
    

