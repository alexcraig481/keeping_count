from django.db import models


class Log(models.Model):
    """A log of unhealthy relationship experiences"""
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Returns a string representation of the model"""
        return f"{self.text}"
