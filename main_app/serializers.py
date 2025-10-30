from rest_framework import serializers
from .models import Challenge, ChallengeMember, Goal,CompletedGoal, User, UserProfile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields = ['username', 'email', 'first_name']
        
class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = UserProfile
        fields = '__all__'
    
class CompletedGoalSerializer(serializers.ModelSerializer):
    class Meta:
        model= CompletedGoal
        fields = '__all__'
        
class ChallengeMemberSerializer(serializers.ModelSerializer):
    completed_goals = CompletedGoalSerializer(many=True, read_only=True)
    class Meta:
        model = ChallengeMember
        fields = '__all__'

class GoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal
        fields = '__all__'
        
class ChallengeSerializer(serializers.ModelSerializer):
    members = ChallengeMemberSerializer(many=True, read_only=True)
    goals = GoalSerializer(many=True, read_only=True)
    # created_by = UserProfileSerializer(read_onl) # it shouldnt be read only because it is a field in this model
    
    class Meta:
        model = Challenge
        fields = '__all__'