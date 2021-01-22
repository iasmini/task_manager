from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=255)
    finished = models.BooleanField(default=False)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
