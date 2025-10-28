from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly

from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

from .models import Challenge, UserProfile, Goal
from .serializers import ChallengeSerializer, GoalSerializer, ChallengeMemberSerializer

User = get_user_model()

class ChallengeIndex(APIView):
    permission_classes = [AllowAny] # just for now

    def get(self, request): # imight make it take user id so i only send a list of user challenges
        try:
            queryset = Challenge.objects.all()
            serializer = ChallengeSerializer(queryset, many=True)
            
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as error:
            return Response({'error':str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def post(self, request):
        try:
            serializer = ChallengeSerializer(data=request.data)
            
            # i will return to this to make the user logged in as the creator by default 
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
        except Exception as error:
                return Response({'error':str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ChallengeDetail(APIView):
    permission_classes = [AllowAny] # just for now
    
    def get(self, request, challenge_id):
        try:
            queryset = get_object_or_404(Challenge, id=challenge_id)
            serializer = ChallengeSerializer(queryset)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as error:
            return Response({'error':str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, challenge_id):
        try:
            queryset = get_object_or_404(Challenge, id=challenge_id)
            serializer = ChallengeSerializer(queryset, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as error:
            return Response({'error':str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, challenge_id):
        try:
            queryset = get_object_or_404(Challenge, id=challenge_id)
            queryset.delete()
            
            return Response({'message':f'challenge {challenge_id} is deleted'})
        except Exception as error:
            return Response({'error':str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class SignUpView(APIView):
    permission_classes = [AllowAny]
    
    def post(self,request):
        try:
            username = request.data.get("username")
            email = request.data.get("email")
            password = request.data.get("password")
            first_name = request.data.get("first_name")
            
            if not username or not email or not password or not first_name:
                return Response({'errors':'Please fill all the sign up fields!'}, status=status.HTTP_400_BAD_REQUEST)
            
            if User.objects.filter(username=username).exists():
                return Response({"error":"username already exist"})
            
            user = User.objects.create_user(
                username=username, email=email, password=password,first_name=first_name
            )
            user_profile = UserProfile.objects.create(user=user)
            
            return Response(
                {"id": user.id, "username": user.username, "email": user.email},
                status=status.HTTP_201_CREATED,
            )
        except Exception as error:
                    return Response({'error':str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class GoalIndex(APIView):
    permission_classes = [AllowAny]
    
    def get(self, request, challenge_id):
        try:
            queryset = Goal.objects.filter(challenge=challenge_id)
            serializer = GoalSerializer(queryset, many=True)
            
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as error:
                return Response({'error':str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
    def post(self, request, challenge_id):
        try:
            serializer = GoalSerializer(data= request.data)
            
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
        except Exception as error:
                return Response({'error':str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class GoalDetail(APIView):
    permission_classes = [AllowAny]
    def get(self, request, challenge_id, goal_id):
        try:
            queryset = get_object_or_404(Goal,id=goal_id)
            serializer = GoalSerializer(queryset)
            
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as error:
                return Response({'error':str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def put(self, request, challenge_id, goal_id):
        try:
            queryset = get_object_or_404(Goal, id=goal_id)
            serializer = GoalSerializer(queryset, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as error:
            return Response({'error':str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def delete(self, request, goal_id):
        try:
            queryset = get_object_or_404(Goal, id=goal_id)
            queryset.delete()
            
            return Response({'message':f'Goal {goal_id} is deleted'})
        except Exception as error:
            return Response({'error':str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
