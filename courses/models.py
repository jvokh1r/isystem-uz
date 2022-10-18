from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=150)
    month = models.IntegerField(default=3)
    day = models.IntegerField(default=3)
    price = models.IntegerField(default=0)
    desc = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title





