from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=4000)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title


class CourseContent(models.Model):
    title = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    content_text = models.TextField()


class Enrollment(models.Model):
    user = models.ForeignKey(User, related_name='enrollments', on_delete=models.CASCADE, )
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrolled_at = models.DateTimeField(auto_now_add=True)


class UserProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    completed_content = models.ManyToManyField(CourseContent)


