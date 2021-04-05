from collections import OrderedDict

from rest_framework import serializers

from .models import Audio
from .models import Content
from .models import Page
from .models import Text
from .models import Video


class NonNullModelSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        result = super(NonNullModelSerializer, self).to_representation(
            instance)
        return OrderedDict(
            [(key, result[key]) for key in result if result[key] is not None])


class VideoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Video
        fields = "__all__"


class AudioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Audio
        fields = "__all__"


class TextSerializer(serializers.ModelSerializer):

    class Meta:
        model = Text
        fields = "__all__"


class ContentSerializer(NonNullModelSerializer):

    video = VideoSerializer()
    audio = AudioSerializer()
    text = TextSerializer()

    class Meta:
        model = Content
        fields = ["video", "audio", "text"]


class PageDetailSerializer(serializers.ModelSerializer):

    content = ContentSerializer(many=True)

    class Meta:
        model = Page
        fields = ['title', 'counter', 'pub_date', "content"]


class PageListSerializer(serializers.HyperlinkedModelSerializer):

    page_detail = serializers.HyperlinkedIdentityField(view_name='app:page-detail')

    class Meta:
        model = Page
        fields = ['title', 'counter', 'pub_date', "page_detail"]
