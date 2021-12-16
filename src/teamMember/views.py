from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .models import teamMember

# Create your views here.

class ListMembersView(ListView):
    model = teamMember #from model we created in model.py
    template_name = 'list.html'

class AddView(CreateView):
    model = teamMember
    template_name = 'add.html'
    fields = '__all__'

class EditView(UpdateView):
    model = teamMember
    template_name = 'edit.html'
    fields = '__all__'
    success_url="/"

class DeleteMemberView(DeleteView):
    model = teamMember
    template_name = 'delete.html'
    success_url="/"