from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.generics import ListAPIView

from profiles.serializers import RegisterSeralizer, UserSeralizer, ProfileSerializer
from profiles.models import Profile

# Create your views here.
class RegisterView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = RegisterSeralizer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.save()
        user_serializer = UserSeralizer(user)
        return Response(user_serializer.data)


class ProfileSearchView(ListAPIView):

    serializer_class = ProfileSerializer

    def get_queryset(self):
        username = self.request.query_params.get('username', '')

        if username:
            return Profile.objects.filter(user__username__icontains=username)
        return Profile.objects.none()