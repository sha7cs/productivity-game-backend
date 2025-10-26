from django.urls import path, include
from .views import ChallengeIndex, ChallengeDetail

urlpatterns = [
    path('challenges/', ChallengeIndex.as_view(), name='all_challenges'),
    path('challenges/<int:challenge_id>/', ChallengeDetail.as_view(), name='challenge_detail')
]
