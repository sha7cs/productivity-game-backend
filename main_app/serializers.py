from rest_framework import serializers
from .models import Challenge, ChallengeMember, Goal,CompletedGoal, User, UserProfile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields = ['id','username', 'email', 'first_name']
    
        
class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    wins_count = serializers.SerializerMethodField()
    class Meta:
        model = UserProfile
        fields = '__all__'
        
    def get_wins_count(self,obj):
        return obj.user.challenges_won.count()
class GoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal
        fields = '__all__'
        
class CompletedGoalSerializer(serializers.ModelSerializer):
    goal_detail = serializers.SerializerMethodField()
    class Meta:
        model= CompletedGoal
        fields = '__all__'
    
    def get_goal_detail(self, obj):
        return GoalSerializer(obj.goal).data
    
class ChallengeMemberSerializer(serializers.ModelSerializer):
    completed_goals = CompletedGoalSerializer(many=True, read_only=True)
    member_info = serializers.SerializerMethodField()
    class Meta:
        model = ChallengeMember
        fields = '__all__'
    def get_member_info(self,obj): # i need to show their names in frontend
        return UserSerializer(obj.user).data
    
class ChallengeSerializer(serializers.ModelSerializer):
    members = ChallengeMemberSerializer(many=True, read_only=True)
    goals = GoalSerializer(many=True, read_only=True)
    winner = UserSerializer(read_only=True)
    
    class Meta:
        model = Challenge
        fields = '__all__'