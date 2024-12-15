from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import Lecture, Speaker, Place
from .serializers import LectureSerializer, SpeakerSerializer, PlaceSerializer

class LectureViewSet(ReadOnlyModelViewSet):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer

class SpeakerViewSet(ReadOnlyModelViewSet):
    queryset = Speaker.objects.all()
    serializer_class = SpeakerSerializer

class PlaceViewSet(ReadOnlyModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
