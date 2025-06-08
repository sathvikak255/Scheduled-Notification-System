from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


class Subscription(models.Model):
    email = models.EmailField(unique=True, default='unknown@example.com')
    start_date = models.DateField()
    end_date = models.DateField()
    formats = models.CharField(max_length=10)  # pdf/html/both
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return f"{self.email} ({self.start_date} to {self.end_date})"
    
    def save(self, *args, **kwargs):
        today = now().date()
        self.is_active = self.start_date <= today <= self.end_date
        super().save(*args, **kwargs)

class ReportHistory(models.Model):
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE)
    date_sent = models.DateField()
    format = models.CharField(max_length=10)  # pdf/html/both
    status = models.CharField(max_length=20)

    def __str__(self):
        return f"Report for {self.subscription.email} on {self.date_sent}"
