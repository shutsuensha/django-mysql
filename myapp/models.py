from django.db import models
from django.db.models import DateTimeField
from django.utils import timezone


class TimestampField(DateTimeField):
    def db_type(self, connection):
        if connection.vendor == "mysql":
            return "timestamp"
        return super().db_type(connection)


class Record(models.Model):
    name = models.CharField(max_length=50)
    date = TimestampField(default=timezone.now)

    def __str__(self):
        return f"{self.name} - {self.date}"
