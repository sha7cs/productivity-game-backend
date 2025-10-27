from rest_framework import serializers
from .models import Challenge, ChallengeMember, Goal

class ChallengeMemberSerializer(serializers.ModelSerializer):
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
    
    class Meta:
        model = Challenge
        fields = '__all__'