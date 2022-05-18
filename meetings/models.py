from django.db import models

# Create your models here.
class Meeting(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, required=True)
    description = models.TextField()

class MeetingType(models.Model):
    ALCHOLICS_ANONYMOUS = "AA"
    NARCOTICS_ANONYMOUS = "NA"
    ALANON = "AL"
    MEETING_CHOICES = [
        (ALCHOLICS_ANONYMOUS,"AA"),
        (NARCOTICS_ANONYMOUS,"NA"),
        (ALANON,"AL"),
    ]
    meeting_type = models.CharField(max_length=2, choices=MEETING_CHOICES, default=ALCHOLICS_ANONYMOUS, required=True)
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE, related_name="type", related_query_name="type")

class Address(models.Model):
    street1 = models.CharField(max_length=200, required=True)
    street2 = models.CharField(max_length=200)
    city = models.CharField(max_length=50, required=True)
    state = models.CharField(max_length=30, required=True)
    zip_code = models.CharField(max_length=20, required=True)
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE, related_name="address")

class Schedule(models.Model):
    meeting_time = models.DateTimeField()
    MONDAY = "Monday"
    TUESDAY = "Tuesday"
    WEDNESDAY = "Wednesday"
    THURSDAY = "Thursday"
    FRIDAY = "Friday"
    SATURDAY = "Saturday"
    SUNDAY = "Sunday"
    MEETING_DAY_CHOICES = [
        (MONDAY,"Monday"),
        (TUESDAY, "Tuesday"),
        (WEDNESDAY, "Wednesday"),
        (THURSDAY, "Thursday"),
        (FRIDAY, "Friday"),
        (SATURDAY, "Saturday"),
        (SUNDAY, "Sunday"),
    ]
    day_of_meeting = models.CharField(max_length=9, choices=MEETING_DAY_CHOICES, required=True)
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE)