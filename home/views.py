from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import TopicSeries, Topics
from .decorators import user_is_superuser
from users.views import profile
from .forms import SeriesCreateForm,TopicsCreateForm,TopicsUpdateForm,SeriesUpdateForm
# Create your views here.
def home(request):
    matching_series = TopicSeries.objects.all()
   
    return render(request=request,
                  template_name='main/home.html',
                  context={"objects": matching_series,"type": "series"}
                  )
def series(request, series:str):
    matching_topics = Topics.objects.filter(topic_slug=series)
   
    return render(request=request,
                  template_name='main/home.html',
                  context={"objects": matching_topics,"type": "topics"}
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
                  template_name='main/navbar.html',
                  context={"object":username}
    )  
    
@user_is_superuser
def new_series(request):
    if request.method=="POST":
      form =SeriesCreateForm(request.POST,request.FILES)
      if form.is_valid():
          form.save()
          return redirect('home')
    else:
        form =SeriesCreateForm()
        
    return render(
        request=request,
        template_name='main/new_record.html',
        context={
            "object": "Series",
            "form": form
            }
        )
@user_is_superuser
def new_post(request):
    if request.method == "POST":
        form = TopicsCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(f"{form.cleaned_data['series'].slug}/{form.cleaned_data.get('topic_slug')}")

    else:
         form = TopicsCreateForm()

    return render(
        request=request,
        template_name='main/new_record.html',
        context={
            "object": "Topic",
            "form": form
            }
        )
@user_is_superuser
def series_update(request, series):
    matching_series = TopicSeries.objects.filter(slug=series).first()

    if request.method == "POST":
        form = SeriesUpdateForm(request.POST, request.FILES, instance=matching_series)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    else:
        form = SeriesUpdateForm(instance=matching_series)

        return render(
            request=request,
            template_name='main/new_record.html',
            context={
                "object": "Series",
                "form": form
                }
            )
@user_is_superuser
def series_delete(request, series):
    matching_series = TopicSeries.objects.filter(slug=series).first()

    if request.method == "POST":
        matching_series.delete()
        return redirect('home')
    else:
        return render(
            request=request,
            template_name='main/confirm_delete.html',
            context={
                "object": matching_series,
                "type": "Series"
                }
            )

@user_is_superuser
def topic_update(request, series, topic):
    matching_topic = Topics.objects.filter(series__slug=series, topic_slug=topic).first()

    if request.method == "POST":
        form = TopicsUpdateForm(request.POST, request.FILES, instance=matching_topic)
        if form.is_valid():
            form.save()
            return redirect(f'/{matching_topic.slug}')
    
    else:
        form = TopicsUpdateForm(instance=matching_topic)

        return render(
            request=request,
            template_name='main/new_record.html',
            context={
                "object": "Topic",
                "form": form
                }
            )

def topic_delete(request, series, topics):
    matching_topics = Topics.objects.filter(series__slug=series, topics_slug=topics).first()

    if request.method == "POST":
        matching_topics.delete()
        return redirect('/')
    else:
        return render(
            request=request,
            template_name='main/confirm_delete.html',
            context={
                "object": matching_topics,
                "type": "topics"
                }
            )          