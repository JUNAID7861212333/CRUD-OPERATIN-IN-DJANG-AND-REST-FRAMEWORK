from django.db import models


# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=100)
    is_complete = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title