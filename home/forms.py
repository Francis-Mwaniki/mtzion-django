from django import forms
from .models import Topics, TopicSeries
from tinymce.widgets import TinyMCE


class NewsletterForm(forms.Form):
    subject = forms.CharField()
    receivers = forms.CharField()
    message = forms.CharField(widget=TinyMCE(), label="Email content")


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
            "speaker",
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