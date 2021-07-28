from django.core.files.base import ContentFile
from login_app import models
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View , TemplateView , ListView , DetailView,CreateView,UpdateView,DeleteView
from my_app1 import models
from django.urls import reverse_lazy
# Create your views here.

# class ClassBasedView(TemplateView):
    # to pass context
    # def get_context_data(self , **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['sample_text1'] = "sample text 1"
    #     context['sample_text2'] = "sample Text 2"
    #     return context

class ClassBasedView(ListView):
    model = models.Musician
    context_object_name = 'musician_list'
    template_name = 'classView/classView.html'

class ClassDetailView(DetailView):
    model = models.Musician
    context_object_name = 'musician'
    template_name = 'classView/detailView.html'

class AddMusician(CreateView):
    model = models.Musician
    fields = ('first_name' , 'last_name' , 'instrument')
    template_name = 'classView/add_musician.html'

class AddMusician(UpdateView):
    model = models.Musician
    fields = ('first_name' , 'instrument')
    template_name = 'classView/add_musician.html'

class DeleteMusician(DeleteView):
    model = models.Musician
    context_object_name = 'musician'
    template_name = 'classView/deleteView.html'
    success_url = reverse_lazy('classBasedView:classBasedView')