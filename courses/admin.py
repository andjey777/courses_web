from django.contrib import admin
from courses.models import CategoryModel, CourseModel, CourseCommentsModel

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    search_fields = ["name"]
    ordering = ("id", "name")


class CourseAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    search_fields = ["name"]
    ordering = ("id", "name")


admin.site.register(CategoryModel, CategoryAdmin)
admin.site.register(CourseModel, CourseAdmin)
admin.site.register(CourseCommentsModel)
