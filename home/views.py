from django.shortcuts import render
from django.http import HttpResponse
from .models import TopicSeries, Topics
from users.views import profile

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
    matching_topic = Topics.objects.filter(series__slug=series, topic_slug=topic).first()
    return render(request=request,
                  template_name='main/article.html',
                  context={"object": matching_topic}
                  )
def nav(request,username):
    username = profile()
    print(username)
    return render(
        request=request,
                  template_name='main/article.html',
                  context={"object":username}
    )        