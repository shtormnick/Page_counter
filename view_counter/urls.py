from django.urls import path
from view_counter.views import PageListView, first
from . import views

urlpatterns = [
   path('', PageListView.as_view()),
   path('', views.first, name='first' ),
]