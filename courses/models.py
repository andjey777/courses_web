from django.conf import settings
from django.db import models

# Create your models here.


class CategoryModel(models.Model):
    categ_name = models.CharField(max_length=50)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.name


class CourseModel(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    rating = models.FloatField()
    category = models.ForeignKey("CategoryModel", on_delete=models.CASCADE)
    times_viewed = models.IntegerField()
    times_completed = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.name


class CourseCommentsModel(models.Model):
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    course = models.ForeignKey("CourseModel", on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now=True)
