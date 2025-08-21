from django.db import models
from django.contrib.auth.models import User

# Stores user’s main fitness info
class FitnessProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age_range = models.CharField(max_length=20)
    weight_range = models.CharField(max_length=20)
    height_range = models.CharField(max_length=20)
    fitness_goal = models.CharField(max_length=50)
    profession = models.CharField(max_length=50)

    # ✅ New fields to store generated values
    bmi = models.FloatField(blank=True, null=True, default=22.0)
    diet_plan = models.TextField(blank=True, null=True, default="Default diet")
    workout_plan = models.TextField(blank=True, null=True, default="Default workout")


    def __str__(self):
        return f"{self.user.username} - {self.fitness_goal}"


# Log user's daily weight with date
class WeightLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    weight = models.FloatField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.date} - {self.weight} kg"


# Store the user's daily workout and diet info
class DailyRoutine(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    workout = models.TextField()
    diet = models.TextField()
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.date}"
