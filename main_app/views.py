from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post, Comment

# Create your views here.
def home(request):
  # Only want home to have  a filter for posts
#   posts = Posts.objects.filter(user=request.user)
  return render(request, 'home.html')

def seekhelp(request):
  posts = Post.objects.all()
  return render(request, 'seekhelp/index.html',{
    'posts':posts
  })

def seekhelpnew(request):
  return render(request, 'seekhelp/new.html')

def seekwork(request):
  return render(request, 'seekwork/index.html')

@login_required
def about(request):
  return render(request, 'about.html')

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('/')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

def post_detail(request, post_id):
  post = Post.objects.get(id=post_id)
  return render(request, 'seekhelp/detail.html', {
    'post':post,
  })

class PostCreate(LoginRequiredMixin, CreateView):
  model = Post
  fields = ['title', 'description', 'rate']
  # success_url = '/seekhelp'
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)
  
class PostUpdate(LoginRequiredMixin, UpdateView):
  model = Post
  fields = '__all__'
  success_url = '/seekhelp'


class PostDelete(LoginRequiredMixin, DeleteView):
  model = Post
  success_url = '/seekhelp'
