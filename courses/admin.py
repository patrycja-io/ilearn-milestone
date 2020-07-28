from django.contrib import admin
from .models import Course, Category

# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

admin.site.register(Course, CourseAdmin)
admin.site.register(Category, CategoryAdmin)
