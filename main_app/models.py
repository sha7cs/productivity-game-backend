from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
import random

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    total_points = models.PositiveIntegerField(default=0)
    total_goals_completed = models.PositiveIntegerField(default=0)
    total_challenges_joined = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.user.username
    
def random_string(): # stack overflow on how to generate unique random value for each object
    return str(random.randint(10000, 99999))

class Challenge(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=300, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING ,  related_name='challenges_created') # keep in mind that i made it do nothing on delete it can cause errors i must handle
    start_date = models.DateField()
    end_date = models.DateField()
    join_code = models.CharField(unique=True, default = random_string)
    is_active = models.BooleanField(default=True)
    winner = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name='challenges_won')
    
    def __str__(self):
        return self.name

class Goal(models.Model):
    title = models.CharField(max_length=150)
    challenge = models.ForeignKey(Challenge, on_delete= models.CASCADE, related_name='goals')
    points = models.PositiveIntegerField()
    description = models.TextField(max_length=320, null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.title} - {self.challenge}'

class ChallengeMember(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE, related_name='challenges_joined')
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE, related_name='members')
    total_points = models.PositiveIntegerField(default=0)
    
    class Meta:
        unique_together = ('challenge', 'user')
        
    def __str__(self):
        return f'{self.challenge} - {self.user}'

class CompletedGoal(models.Model):
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE, related_name='completed_goals')
    challenge_member = models.ForeignKey(ChallengeMember , on_delete=models.CASCADE , related_name='completed_goals')
    completion_date = models.DateField(auto_now_add=True)
    # proof = models.ImageField() # will see it later since it's optional
    
    def __str__(self):
        return f'{self.goal} completed by {self.challenge_member}'