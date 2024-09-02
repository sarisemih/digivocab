from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.generics import ListAPIView
from rest_framework import status

from profiles.serializers import RegisterSeralizer, UserSeralizer, ProfileSerializer
from profiles.models import Profile, FollowRelation

from django.shortcuts import get_object_or_404
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
    

class FollowProfileView(APIView):
    
    def post(self, request, username):
        profile_to_follow = get_object_or_404(Profile, user__username=username)
        
        # Check if the user is trying to follow themselves
        if request.user.profile == profile_to_follow:
            return Response({'error': "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)
        
        # Attempt to create the follow relation, which will do nothing if it already exists
        _, created = FollowRelation.objects.get_or_create(follower=request.user.profile, following=profile_to_follow)
        
        if created:
            return Response({"success": "User followed successfully"}, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': "You are already following this user."}, status=status.HTTP_400_BAD_REQUEST)
    
class UnfollowProfileView(APIView):
    
    def post(self, request, username):
        profile_to_unfollow = get_object_or_404(Profile, user__username=username)

        follow_relation = FollowRelation.objects.filter(follower=request.user.profile, following=profile_to_unfollow)
        if follow_relation.exists(): 
            follow_relation.delete()
            return Response({"succes":"User unfollowed succesfully"})
        
        if request.user.profile == profile_to_unfollow:
            return Response({'error':"You can not unfollow yourself."}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'error': "You are already unfollowing this user."}, status=status.HTTP_400_BAD_REQUEST)
    
class FollowedListView(ListAPIView):
    
    serializer_class = ProfileSerializer

    def get_queryset(self):
        user_profile = self.request.user.profile
        return user_profile.followers.all()
