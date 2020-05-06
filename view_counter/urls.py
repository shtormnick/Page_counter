from django.urls import path
from view_counter.views import PageListView 

urlpatterns = [
   path('', PageListView.as_view()),
]