from django.urls import path
from view_counter.views import PageListView, PageDetail


urlpatterns = [
   path('', PageListView.as_view()),
   path('page/<pk>/', PageDetail.as_view()),
]