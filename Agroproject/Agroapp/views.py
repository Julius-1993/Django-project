from django.shortcuts import render
from .forms import Clientform
#from django.http import HttpResponse
def index(response):
  return render(response, "Agroapp/index.html", {})

def about(response):
  return render(response, "Agroapp/about.html", {})

def registration(response):
  if response.method == 'POST':
    form = Clientform(response.POST or None)
    if form.is_valid():
      form.save()
      form = Clientform()
  context = {
    'form': Clientform
  }
  return render(response, "Agroapp/registration.html", context)
