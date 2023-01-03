from django.shortcuts import render
from django.http import HttpResponse
from .models import TopicSeries, Topics

# Create your views here.
def home(request):
    matching_series = TopicSeries.objects.all()
   
    return render(request=request,
                  template_name='main/home.html',
                  context={"objects": matching_series}
                  )
def series(request, series:str):
    matching_topics = Topics.objects.filter(topic_slug=series)
   
    return render(request=request,
                  template_name='main/home.html',
                  context={"objects": matching_topics}
                  )
def topic(request, series: str, topic: str):
    matching_topic = Topics.objects.filter(series__slug=series, topic_slug=topic)
    return render(request=request,
                  template_name='main/article.html',
                  context={"object": matching_topic}
                  )    