from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from vocabularies.serializers import VocabularySerializer, WordSerializers
from vocabularies.models import Vocabulary, Word
from vocabularies.permissions import IsOwnerOrReadOnly, IsOwnerOfVocabularyOrReadOnly

from profiles.models import Profile

class VocabularyListCreateView(ListCreateAPIView):
    serializer_class =  VocabularySerializer
    
    def get_queryset(self):

        profile_id = self.request.query_params.get('profile_id')
        
        if profile_id:
            profile = get_object_or_404(Profile, id=profile_id)
        else:
            profile = self.request.user.profile
        profile = get_object_or_404(Profile, user=self.request.user)
        queryset = Vocabulary.objects.filter(profile=profile)

        return queryset
    
    def perform_create(self, serializer):
        serializer.save(profile=self.request.user.profile)


class VocabularyDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Vocabulary.objects.all()
    serializer_class = VocabularySerializer
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]
    lookup_field = "id"


class WordListCreateView(ListCreateAPIView):
    serializer_class = WordSerializers
    
    def get_queryset(self):
        vocabulary_id = self.kwargs.get('vocabulary_id')
        vocabulary = get_object_or_404(Vocabulary, id=vocabulary_id)

        return Word.objects.filter(vocabulary= vocabulary)
    
    def perform_create(self, serializer):
        
        vocabulary_id = self.kwargs.get('vocabulary_id')
        vocabulary = get_object_or_404(Vocabulary, id=vocabulary_id, profile=self.request.user.profile)

        serializer.save(vocabulary=vocabulary)


class WordDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = WordSerializers
    queryset = Word.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOfVocabularyOrReadOnly]

    def get_object(self):
        
        vocabulary_id = self.kwargs.get('vocabulary_id')
        word_id = self.kwargs.get('word_id')

        word = get_object_or_404(Word, id=word_id, vocabulary_id=vocabulary_id)
        self.check_object_permissions(self.request, word)

        return word


class CopyVocabularyView(APIView):

    def post(self, request, vocabulary_id):
        original_vocabulary = get_object_or_404(Vocabulary, id=vocabulary_id)
        copied_vocabulary = Vocabulary.objects.create(
            name = f"Copy of {original_vocabulary.name}",
            description = original_vocabulary.description,
            profile=request.user.profile  

        )

        words = Word.objects.filter(vocabulary=original_vocabulary)

        for word in words:
            Word.objects.create(
                vocabulary=copied_vocabulary, 
                text=word.text,
                meaning=word.meaning,
                example_sentence=word.example_sentence 
            )
        return Response({
            "succes": "Vocabulary copied succesfully."
        })