from django.db import models
from django.urls import reverse
from datetime import date, datetime
from django.contrib.auth.models import User
# Create your models here.

STATUS = (
    ('n', 'New'),
    ('i', 'In Progress'),
    ('c', 'Complete')
)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=500)
    timestamp = models.DateTimeField(default=datetime.now)


class Post(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField(max_length=250)
    rate = models.IntegerField()
    status = models.CharField(
        max_length=1,
        choices=STATUS,
        default=STATUS[0][0]
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comments = models.ManyToManyField(Comment)


# Use https://git.generalassemb.ly/SEIR-01-23/student_resources/blob/main/unit_3/week_2/day_5/lessons/django_authentication.md
# part 8 to associate user with post

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('seekhelp')

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_business = models.BooleanField()

    

