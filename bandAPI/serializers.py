from rest_framework import serializers
from bandAPI.models import Band, Album, Song

class BandSerializer(serializers.HyperlinkedModelSerializer):
	"""Serializes bands"""
	albums = serializers.StringRelatedField(many=True)

	class Meta:
		model = Band
		fields = ('id', 'url', 'name', 'origin', 'date_formed', 'albums')
		lookup_field = 'name'
		extra_kwargs = {
			'url': {'lookup_field': 'name'}
		}

class AlbumSerializer(serializers.HyperlinkedModelSerializer):
	band = serializers.StringRelatedField()
	songs = serializers.StringRelatedField(many=True)

	class Meta:
		model = Album
		fields = ('id', 'url', 'title', 'date_released', 'run_time', 'band', 'songs')
		lookup_field = 'title'
		extra_kwargs = {
			'url': {'lookup_field': 'title'}
		}

class SongSerializer(serializers.HyperlinkedModelSerializer):
	album = serializers.StringRelatedField()

	class Meta:
		model = Song
		fields = ('id', 'url', 'title', 'length', 'album')
		lookup_field = 'title'
		extra_kwargs = {
			'url': {'lookup_field': 'title'}
		}