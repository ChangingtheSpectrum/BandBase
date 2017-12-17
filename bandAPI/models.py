from django.db import models

class Band(models.Model):
	name = models.CharField(max_length=100, null=False)
	origin = models.CharField(max_length=100, null=True)
	date_formed = models.DateField()

	def __str__(self):
		return self.name

class Album(models.Model):
	title = models.CharField(max_length=100, null=False)
	date_released = models.DateField()
	run_time = models.DurationField()
	band = models.ForeignKey(
		Band,
		related_name='albums',
		on_delete=models.CASCADE,
	)

	def __str__(self):
		return self.title

class Song(models.Model):
	title = models.CharField(max_length=100, null=False)
	length = models.DurationField()
	album = models.ForeignKey(
		'Album',
		related_name='songs',
		on_delete=models.CASCADE,
	)

	def __str__(self):
		return self.title