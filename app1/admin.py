from django.contrib import admin

# Register your models here.
from . import models
admin.site.register(models.personal_information)
admin.site.register(models.profesional_details)
admin.site.register(models.Projects)
