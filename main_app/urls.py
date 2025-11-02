from django.urls import path, include
from .views import ChallengeIndex, ChallengeDetail, SignUpView, GoalIndex, GoalDetail, LeaveChallenge, JoinChallenge,MakeCompletedGoal, CompleteGoalIndex
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
urlpatterns = [
    path('challenges/', ChallengeIndex.as_view(), name='all_challenges'),
    path('challenges/<int:challenge_id>/', ChallengeDetail.as_view(), name='challenge_detail'),
    path('challenges/<int:challenge_id>/goals/', GoalIndex.as_view(), name='challenge_goals'),
    path('challenges/<int:challenge_id>/goals/<int:goal_id>/', GoalDetail.as_view(), name='goal_detail'),
    path('challenges/<int:challenge_id>/delete-member/<int:member_id>/', LeaveChallenge.as_view(), name='delete_member'),
    path('challenges/join/', JoinChallenge.as_view(), name='member_joins'),
    path('challenges/<int:challenge_id>/goals/<int:goal_id>/complete/', MakeCompletedGoal.as_view(), name='complete_goal'),
    path('challenges/<int:challenge_id>/goals/complete/', CompleteGoalIndex.as_view(), name='complete_goal_index'),
    # Auth
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('signup/', SignUpView.as_view(), name="signup")
]
