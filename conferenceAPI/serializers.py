from rest_framework import serializers
from .models import Place, Speaker, Lecture

class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields', None)
        exclude = kwargs.pop('exclude', None)

        super().__init__(*args, **kwargs)

        if fields is not None:
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)

        if exclude is not None:
            for field_name in exclude:
                self.fields.pop(field_name, None)


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ['id', 'building_name', 'room_name']

class SpeakerSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Speaker
        fields = ['id', 'name', 'surname', 'description']

class LectureSerializer(serializers.ModelSerializer):
    place_id = PlaceSerializer()
    speakers = SpeakerSerializer(many=True, exclude=['description'])

    class Meta:
        model = Lecture
        fields = ['id', 'begin_time', 'end_time', 'description', 'title', 'place_id', 'speakers']