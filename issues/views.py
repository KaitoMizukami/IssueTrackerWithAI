from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Issue


class IssueListView(ListView):
    model = Issue
    template_name = 'issues/list.html'
    context_object_name = 'issues'