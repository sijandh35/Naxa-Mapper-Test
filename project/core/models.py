from django.db import models
from django.conf import settings
from django.contrib.postgres.fields import JSONField


# Create your models here.
class BaseMap(models.Model):
    photo = models.ImageField(blank=True, null=True)
    title = models.CharField(max_length=500, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.title


class ProjectType(models.Model):
    title = models.CharField(max_length=500, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    thumbnail = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.title


class Project(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    project_type_id = models.ForeignKey(ProjectType, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=500, blank=True, null=True)
    layer_order = models.JSONField(blank=True, null=True)
    layers = models.JSONField(blank=True, null=True)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    thumbnail = models.ImageField(blank=True, null=True)
    is_public = models.BooleanField(null=True, blank=True)
    base_map_id = models.ForeignKey(BaseMap, on_delete=models.CASCADE, blank=True, null=True)
    layout_metadata = models.JSONField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.title


class Layer(models.Model):
    styles = models.JSONField(blank=True, null=True)
    name = models.CharField(max_length=500, blank=True, null=True)
    data_type = models.CharField(max_length=500, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    is_public = models.BooleanField(null=True, blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    metadata = models.JSONField(blank=True, null=True)

    def __str__(self):
        return self.name
