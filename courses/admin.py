from django.contrib import admin

from courses.models import (
    CategoryModel,
    CourseCommentsModel,
    CourseModel,
)

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    search_fields = ["name"]
    ordering = ("id", "name")
    readonly_fields = ("date_created", "last_modified")


class CourseAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    search_fields = ["name"]
    ordering = ("id", "name")
    readonly_fields = ("date_created", "last_modified")


admin.site.register(CategoryModel, CategoryAdmin)
admin.site.register(CourseModel, CourseAdmin)
admin.site.register(CourseCommentsModel)
