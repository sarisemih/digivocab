from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from profiles.serializers import RegisterSeralizer, UserSeralizer

# Create your views here.
class RegisterView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = RegisterSeralizer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.save()
        user_serializer = UserSeralizer(user)
        return Response(user_serializer.data)
