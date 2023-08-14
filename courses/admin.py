from django.contrib import admin
from .models import Course, CourseContent, Tag


admin.site.register(Course)
admin.site.register(CourseContent)
admin.site.register(Tag)
