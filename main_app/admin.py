from django.contrib import admin
from .models import UserProfile, Challenge, Goal , CompletedGoal, ChallengeMember

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Challenge)
admin.site.register(Goal)
admin.site.register(CompletedGoal)
admin.site.register(ChallengeMember)
