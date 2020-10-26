from django.db import models


class Person(models.Model):
    last_name = models.CharField(max_length=130)
    first_name = models.CharField(max_length=130)
    email = models.EmailField(blank=True)
    job_title = models.CharField(max_length=30, blank=True)
    bio = models.TextField(blank=True)
