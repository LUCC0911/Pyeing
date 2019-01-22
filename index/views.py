from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Tweet
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.urls import reverse


def top(request):
    return render(request, 'index/top.html')

def tweet_list(request):
    tweets = Tweet.objects.all()
    return render(request, 'index/tweet_list.html', {'tweets':tweets})

@login_required
def profile(request):
    return render(request, 'index/profile.html')
    

def help(request):
    return render(request, 'index/help.html')

def tweet_add(request):
    if request.method == 'POST':
        t = Tweet(id=len(Tweet.objects.order_by('-id'))+1, content=request.POST['content'], user=request.user, update_date=timezone.now())
        t.save()
        return HttpResponseRedirect(reverse('tweet_list'))
    return render(request, 'index/tweet_add.html')

def policy(request):
    return render(request, 'index/policy.html')