from django.db import models
from django.utils import timezone

# Create your models here.
class Job(models.Model):
    repo_url = models.URLField(max_length=2000, null=True)
    status = models.BooleanField(default = False)
    run_date = models.DateTimeField(null = True, blank = True)
    date_created = models.DateTimeField(default = timezone.now())
