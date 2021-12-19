from django.contrib import admin
from category.models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'category_name',
        'slug'
    )
    list_display_links = list_display
