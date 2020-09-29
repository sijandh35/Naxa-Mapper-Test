from django.contrib import admin
from .models import ProjectType, Project, Category, BaseMap, Layer

# Register your models here.


admin.site.register(Project)
admin.site.register(Category)
admin.site.register(BaseMap)
admin.site.register(Layer)
admin.site.register(ProjectType)
