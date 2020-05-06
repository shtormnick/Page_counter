from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from view_counter.models import Page

# Create your views here.

class PageListView(ListView):
    model = Page


def first(request):
    return HttpResponse('first page')