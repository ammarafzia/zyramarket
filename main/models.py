from django.db import models


class MoodEntry(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    stock = models.IntegerField()

    @property
    def is_mood_strong(self):
        return self.mood_intensity > 5