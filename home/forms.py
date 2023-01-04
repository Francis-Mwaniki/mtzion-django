from django import forms
from .models import Topics, TopicSeries

class SeriesCreateForm(forms.ModelForm):
    class Meta:
        model = TopicSeries

        fields = [
            "title",
            "subtitle",
            "slug",
            "image",
        ]

class TopicsCreateForm(forms.ModelForm):
    class Meta:
        model = Topics

        fields = [
            "title",
            "subtitle",
            "topic_slug",
            "content",
            "notes",
            "series",
            "image",
        ]

class SeriesUpdateForm(forms.ModelForm):
    class Meta:
        model = TopicSeries

        fields = [
            "title",
            "subtitle",
            "image",
        ]

class TopicsUpdateForm(forms.ModelForm):
    class Meta:
        model = Topics

        fields = [
            "title",
            "subtitle",
            "content",
            "speaker",
            "series",
            "image",
        ]