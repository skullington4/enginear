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

class Post(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField(max_length=250)
    rate = models.IntegerField()
    status = models.CharField(
        max_length=1,
        choices=STATUS,
        default=STATUS[0][0]
    )
    is_business = models.BooleanField(default=False)
    timestamp = models.DateTimeField(default=datetime.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-timestamp']

# Use https://git.generalassemb.ly/SEIR-01-23/student_resources/blob/main/unit_3/week_2/day_5/lessons/django_authentication.md
# part 8 to associate user with post

    def __str__(self):
        return f'{self.get_status_display()} on {self.title}'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'post_id':self.id})

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # is_business = models.BooleanField(default=False)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=500)
    timestamp = models.DateTimeField(default=datetime.now)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
    # Nice method for obtaining the friendly value of a Field.choice
        return f"{self.get_description_display()} on {self.timestamp}"
  
    def get_absolute_url(self):
        return reverse('detail', kwargs={'post_id':self.post_id})

    class Meta:
        ordering = ['-timestamp']