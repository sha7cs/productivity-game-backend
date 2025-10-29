from django.urls import path, include
from .views import ChallengeIndex, ChallengeDetail, SignUpView, GoalIndex, GoalDetail, ChallengeMemberAdd, ChallengeMemberDelete
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
urlpatterns = [
    path('challenges/', ChallengeIndex.as_view(), name='all_challenges'),
    path('challenges/<int:challenge_id>/', ChallengeDetail.as_view(), name='challenge_detail'),
    path('challenges/<int:challenge_id>/goals/', GoalIndex.as_view(), name='challenge_goals'),
    path('challenges/<int:challenge_id>/goals/<int:goal_id>/', GoalDetail.as_view(), name='goal_detail'),
    path('challenges/<int:challenge_id>/add-user/<int:user_id>/', ChallengeMemberAdd.as_view(), name='add_member'),
    path('challenges/<int:challenge_id>/delete-member/<int:member_id>/', ChallengeMemberDelete.as_view(), name='delete_member'),
    # Auth
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('signup/', SignUpView.as_view(), name="signup")
]
