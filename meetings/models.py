from django.db import models

# Create your models here.
class Meeting(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, required=True)
    description = models.TextField()
    meeting_type = models.CharField(max_length=30)
    meeting_time = models.DateTimeField(editable=True)
    meeting_day = models.CharField(max_length=20)

