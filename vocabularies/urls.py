from django.urls import path

from vocabularies.views import VocabularyListCreateView
urlpatterns = [
    path('', VocabularyListCreateView.as_view(), name='vocabularies'),

]