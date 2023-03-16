from django.shortcuts import render

# Create your views here.
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

def findhelp(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'findhelp/index.html')

def findwork(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'findwork/index.html')


def about(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'about.html')
