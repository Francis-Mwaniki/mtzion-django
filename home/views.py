import os
from uuid import uuid4
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import TopicSeries, Topics
from .decorators import user_is_superuser
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from users.views import profile
from .forms import SeriesCreateForm,TopicsCreateForm,TopicsUpdateForm,SeriesUpdateForm,NewsletterForm
from django.contrib import messages
from django.core.mail import EmailMessage
from users.models import SubscribedUsers


@user_is_superuser
def newsletter(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data.get('subject')
            receivers = form.cleaned_data.get('receivers').split(',')
            email_message = form.cleaned_data.get('message')

            mail = EmailMessage(subject, email_message, f"Francis Mwaniki <{request.user.email}>", bcc=receivers)
            mail.content_subtype = 'html'

            if mail.send():
                messages.success(request, "Email sent successfully")
            else:
                messages.error(request, "There was an error sending email")

        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

        return redirect('/')

    form = NewsletterForm()
    form.fields['receivers'].initial = ','.join([active.email for active in SubscribedUsers.objects.all()])
    return render(request=request, template_name='main/newsletter.html', context={'form': form})

# Create your views here.
def home(request):
    matching_series = TopicSeries.objects.all()
   
    return render(request=request,
                  template_name='main/home.html',
                  context={"objects": matching_series,"type": "series"}
                  )
def series(request, series:str):
    matching_topics = Topics.objects.filter(series__slug=series).all()
   
    return render(request=request,
                  template_name='main/home.html',
                  context={"objects": matching_topics,"type": "topics"}
                  )
def topic(request, series: str, topic: str):
    matching_topic = Topics.objects.filter(series__slug=series, topic_slug=topic).first()
    return render(request=request,
                  template_name='main/topic.html',
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
            return redirect('home')
    
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

def topic_delete(request, series, topic):
    matching_topics = Topics.objects.filter(series__slug=series, topic_slug=topic).first()

    if request.method == "POST":
        matching_topics.delete()
        return redirect('home')
    else:
        return render(
            request=request,
            template_name='main/confirm_delete.html',
            context={
                "object": matching_topics,
                "type": "topics"
                }
            )          
        
@csrf_exempt
@user_is_superuser
def upload_image(request, series: str=None, topic: str=None):
    if request.method != "POST":
        return JsonResponse({'Error Message': "Wrong request"})

    # If it's not series and not topic, handle it differently
    matching_topic = Topics.objects.filter(series__slug=series, topic_slug=topic).first()
    if not matching_topic:
        return JsonResponse({'Error Message': f"Wrong series ({series}) or topic ({topic})"})

    file_obj = request.FILES['file']
    file_name_suffix = file_obj.name.split(".")[-1]
    if file_name_suffix not in ["jpg", "png", "gif", "jpeg"]:
        return JsonResponse({"Error Message": f"Wrong file suffix ({file_name_suffix}), supported are .jpg, .png, .gif, .jpeg"})

    file_path = os.path.join(settings.MEDIA_ROOT, 'TopicSeries', matching_topic.slug, file_obj.name)
    
    if os.path.exists(file_path):
        file_obj.name = str(uuid4()) + '.' + file_name_suffix
        file_path = os.path.join(settings.MEDIA_ROOT, 'TopicSeries', matching_topic.slug, file_obj.name)
        
    with open(file_path, 'wb+') as f:
        for chunk in file_obj.chunks():
            f.write(chunk)

        return JsonResponse({
            'message': 'Image uploaded successfully',
            'location': os.path.join(settings.MEDIA_URL, 'TopicSeries', matching_topic.slug, file_obj.name)
        })   