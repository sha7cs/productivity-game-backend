from django.urls import path, include
from .views import ChallengeIndex

urlpatterns = [
    path('challenges/', ChallengeIndex.as_view(), name='all_challenges')
]
