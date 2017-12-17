from bandAPI.models import Band, Album, Song
from bandAPI.serializers import BandSerializer, AlbumSerializer, SongSerializer
from rest_framework import generics, viewsets

#class BandList(generics.ListCreateAPIView):
	#queryset = Band.objects.all()
	#serializer_class = BandSerializer

#class BandDetail(generics.RetrieveUpdateDestroyAPIView):
	#queryset = Band.objects.all()
	#serializer_class = BandSerializer

#class AlbumList(generics.ListCreateAPIView):
	#queryset = Album.objects.all()
	#serializer_class = AlbumSerializer

#class AlbumDetail(generics.RetrieveUpdateDestroyAPIView):
	#queryset = Album.objects.all()
	#serializer_class = AlbumSerializer

#class SongList(generics.ListCreateAPIView):
	#queryset = Song.objects.all()
	#serializer_class = SongSerializer

#class SongDetail(generics.RetrieveUpdateDestroyAPIView):
	#queryset = Song.objects.all()
	#serializer_class = SongSerializer

class BandViewSet(viewsets.ModelViewSet):
	queryset = Band.objects.all()
	serializer_class = BandSerializer
	lookup_field = ('name')

class AlbumViewSet(viewsets.ModelViewSet):
	queryset = Album.objects.all()
	serializer_class = AlbumSerializer
	lookup_field = ('title')

class SongViewSet(viewsets.ModelViewSet):
	queryset = Song.objects.all()
	serializer_class = SongSerializer
	lookup_field = ('title')