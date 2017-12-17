from django.conf.urls import url, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'bands', views.BandViewSet)
router.register(r'albums', views.AlbumViewSet)
router.register(r'songs', views.SongViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]