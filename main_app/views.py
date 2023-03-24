from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post, Comment, User
from .forms import CommentForm, WorkForm



def home(request):
  if (request.user.is_authenticated):
    posts = Post.objects.filter(user=request.user)
  else:
    posts = None
  return render(request, 'home.html', {
      'posts':posts
    })

def seekhelp(request):
  posts = Post.objects.filter(is_business=True)
  final_posts = posts.filter(status='n')
  return render(request, 'seekhelp/index.html',{
    'posts':final_posts
  })

def seekwork(request):
  posts = Post.objects.filter(is_business=False)
  final_posts = posts.filter(status='n')
  return render(request, 'seekwork/index.html',{
    'posts':final_posts
  })

def about(request):
  return render(request, 'about.html')

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('/')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

def post_detail(request, post_id):
  post = Post.objects.get(id=post_id)
  comment_form = CommentForm()
  user_id = request.user.id
  return render(request, 'seekhelp/detail.html', {
    'post':post,
    'comment_form': comment_form,
    'user_id':user_id
  })

class PostCreate(LoginRequiredMixin, CreateView):
  model = Post
  fields = ['title', 'description', 'rate', 'is_business' ]
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)
  
class PostUpdate(LoginRequiredMixin, UpdateView):
  model = Post
  fields = ['title', 'description', 'rate', 'is_business', 'status' ]

class PostDelete(LoginRequiredMixin, DeleteView):
  model = Post
  success_url = '/'


def add_comment(request, post_id):
  form = CommentForm(request.POST)
  if form.is_valid():
    new_comment = form.save(commit=False)
    new_comment.post_id = post_id
    new_comment.user = request.user
    new_comment.save()
  return redirect('detail', post_id=post_id)


class CommentUpdate(LoginRequiredMixin, UpdateView):
  model = Comment
  fields = ['description']
  

class CommentDelete(LoginRequiredMixin, DeleteView):
  model = Comment
  def get_success_url(self):
    post = Post.objects.get(pk=self.object.post.pk)
    return post.get_absolute_url()