from django.contrib import admin
from .models import Todo, Category, Tag


class TodoAdmin(admin.ModelAdmin):
    list_display = [
        'pk', # Primaey Key(id)
        'user',
        'title',
        'category',
        'is_active',
        'created_at',
        'updated_at',
    ]
    list_display_links = [ # Admin panelinde gösterilenlerden hangilerini tıklanabilir olmasını sağlar.
        'pk',
        'title',
        'category',
    ]




class CategoryAdmin(admin.ModelAdmin):
    list_display=[
        'pk',
        'title',
        'slug',
        'is_active',
    ]
    list_display_links = [
        'pk',
        'title',
    ]

class TagAdmin(admin.ModelAdmin):
    list_display=[
        'pk',
        'title',
        'slug',
    ]
    list_display_links=[
        'pk',
        'title',
    ]



admin.site.register(Todo, TodoAdmin,)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)