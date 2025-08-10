from django.db import models
import datetime
# Create your models here.
class CaseData(models.Model):
    case_type = models.CharField(max_length=50)
    case_number = models.CharField(max_length=100, unique=True)
    year = models.CharField(max_length=10)
    result = models.TextField()
    log_time = models.DateTimeField(default=datetime.datetime.now)