from django.shortcuts import render

# Create your views here.
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

def seekinghelp(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'seekinghelp/index.html')

def seekingwork(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'seekingwork/index.html')


def about(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'about.html')
