from django.contrib import admin
from .models import Page, Counter

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    pass

@admin.register(Counter)
class CounterAdmin(admin.ModelAdmin):
    pass