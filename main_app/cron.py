from .models import Challenge, ChallengeMember
from datetime import date


# since the winner is assigned when a challenge reaches its ending date i wanted to do something atomatic that checks 
# it will be ru everyday at midnight to see it any challenge ended then calculates the winner then adds it 

# i made use of this persons question https://forum.djangoproject.com/t/django-scheduler/18526 
# i also watched this video to see how can i use it https://youtu.be/6eoS9CFOmFw?si=JFuXF8-DuqywV1UR
def assign_winner():
    today = date.today()
    done_challenges = Challenge.objects.filter(end_date__lt=today, winner__isnull=True)
    
    for challenge in done_challenges:
        members = ChallengeMember.objects.filter(challenge=challenge)
        top_member = members.order_by('-total_points').first()
        
        if top_member: # i want to handle it there is a tie , but will leave it for later
            challenge.winner = top_member.user
            challenge.is_active =False
            challenge.save()