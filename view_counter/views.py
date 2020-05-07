from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from view_counter.models import Page, Counter

# Create your views here.

class PageListView(ListView):
    model = Page


class PageDetail(DetailView):
    model = Page
    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        is_visit = request.COOKIES.get('is_visit')
        if is_visit is None:
            counter, created = Counter.objects.get_or_create(page=self.object)
            counter.count += 1 
            counter.save()
            response.set_cookie('is_visit', True, path=request.get_full_path)
        
        return response