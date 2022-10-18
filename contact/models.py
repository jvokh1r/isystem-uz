from django.db import models
from courses.models import Course

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    msg = models.TextField()

    is_solved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Apply(models.Model):
    name = models.CharField(max_length=221)
    age = models.IntegerField()
    phone = models.IntegerField()
    extra_phone = models.IntegerField()
    course_choice = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
