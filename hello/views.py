from django.shortcuts import render
from django.views.generic.base import  TemplateView
from .models import  Hello
from django.utils.inspect import func_accepts_kwargs
from lib2to3.fixes.fix_input import context
from django.views.generic import ListView,DetailView


class IndexView(TemplateView):
    template_name = "index.html"
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['one_name'] = Hello.objects.all()[0]
        return context
class NameListView(ListView):
    model = Hello
    
class NameDetailView(DetailView):
    model = Hello

#from django.http import  HttpResponse


#def index(request):
 #   return HttpResponse("Hello Django")

# Create your views here.
