from django.contrib import admin
from django.contrib.admin import ModelAdmin

from scores import models


class StudentAdmin(ModelAdmin):
    list_display = ["first_name", "last_name", "age", "created_at", "updated_at"]


class SubjectAdmin(ModelAdmin):
    list_display = ["name", "code", "created_at", "updated_at"]


class TestAdmin(ModelAdmin):
    list_display = ["title", "subject", "max_score", "created_at", "updated_at"]

admin.site.register(models.Student, StudentAdmin)
admin.site.register(models.Subject, SubjectAdmin)
admin.site.register(models.Test, TestAdmin)
admin.site.register(models.Score)
