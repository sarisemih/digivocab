from rest_framework.generics import ListCreateAPIView

from django.shortcuts import get_object_or_404

from vocabularies.serializers import VocabularySerializer
from vocabularies.models import Vocabulary

from profiles.models import Profile

class VocabularyListCreateView(ListCreateAPIView):
    serializer_class =  VocabularySerializer
    
    def get_queryset(self):
        profile = get_object_or_404(Profile, user=self.request.user)
        queryset = Vocabulary.objects.filter(profile=profile)

        return queryset
    
    def perform_create(self, serializer):
        serializer.save(profile=self.request.user.profile)