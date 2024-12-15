from django.db import models

class Place(models.Model):
    building_name = models.CharField(max_length=100)
    room_name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return "%s %s %s" % (self.pk, self.building_name, self.room_name)


class Speaker(models.Model):
    name = models.CharField(max_length=80)
    surname = models.CharField(max_length=160)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return "%s %s %s" % (self.pk, self.name, self.surname)


class Lecture(models.Model):
    begin_time = models.DateTimeField()
    end_time = models.DateTimeField()
    description = models.TextField(null=True, blank=True)
    title = models.CharField(max_length=200)
    place_id = models.ForeignKey('Place', on_delete=models.CASCADE)
    speakers = models.ManyToManyField(Speaker, related_name='lectures')

    def __str__(self):
        return "%s %s" % (self.pk, self.title)