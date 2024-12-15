from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LectureViewSet, SpeakerViewSet, PlaceViewSet

router = DefaultRouter()
router.register(r'lectures', LectureViewSet)
router.register(r'speakers', SpeakerViewSet)
router.register(r'places', PlaceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]