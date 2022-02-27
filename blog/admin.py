from django.contrib import admin

# Register your models here.
from blog.models import Category,Tag


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','status','is_nav','owner','create_time')
    fields = ('name','status','is_nav','owner')


@admin.register(Tag)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','status','owner','create_time')
    fields = ('name','status','owner')
