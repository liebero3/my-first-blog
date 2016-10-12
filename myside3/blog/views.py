#def homepage(request):
#    if request.user.is_anonymous():
#
#    else:


from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import Group

# Create your views here.
#@user_passes_test(lambda u: Group.objects.get(name='EFPHGK2') in u.groups.all())
def post_list(request):
    posts = Post.objects.filter(pdate__lte=timezone.now())#.order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, digit):
    single_post = Post.objects.filter(id=digit)
    print(single_post)
    return render(request, 'blog/post_detail.html', {'single_post': single_post})

def show_homepage(request):
    return render(request, 'blog/index.html')
