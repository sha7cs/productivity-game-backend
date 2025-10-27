from django.urls import path, include
from .views import ChallengeIndex, ChallengeDetail, SignUpView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
urlpatterns = [
    path('challenges/', ChallengeIndex.as_view(), name='all_challenges'),
    path('challenges/<int:challenge_id>/', ChallengeDetail.as_view(), name='challenge_detail'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('signup/', SignUpView.as_view(), name="signup")
]
