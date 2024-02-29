from django.http import HttpResponse
from rest_framework import status, serializers
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from profiles.models import Profile
from profiles.selectors import ProfileSelector
from profiles.services import ProfileService


class CreateProfileView(APIView):
    permission_classes = [AllowAny]

    class CreateProfileSerializer(serializers.Serializer):
        email = serializers.EmailField(required=True)

    def post(self, request, *args, **kwargs) -> HttpResponse:
        serializer = self.CreateProfileSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        ProfileService().create_profile(Profile(**serializer.validated_data))
        return Response({"message": "Please check your email for validation!"}, status=status.HTTP_201_CREATED)


class AllProfilesView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs) -> HttpResponse:
        profiles = ProfileSelector().get_all_profiles()
        return Response({"profiles": profiles})
