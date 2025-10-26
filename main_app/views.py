from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Challenge, Goal
from .serializers import ChallengeSerializer

class ChallengeIndex(APIView):
    
    def get(self, request):
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
        