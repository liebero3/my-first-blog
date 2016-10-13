#def homepage(request):
#    if request.user.is_anonymous():
#
#    else:


from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.http import *
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
#from birthdayreminder.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import Group

# Create your views here.
#@user_passes_test(lambda u: Group.objects.get(name='EFPHGK2') in u.groups.all())
@login_required(login_url='/login/')
def post_list(request):
    posts = Post.objects.filter(pdate__lte=timezone.now())#.order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
@login_required(login_url='/login/')
def post_detail(request, digit):
    single_post = Post.objects.filter(id=digit)
    return render(request, 'blog/post_detail.html', {'single_post': single_post})

def show_homepage(request):
    return render(request, 'blog/index.html')

def login_user(request):
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('blog/post_list.html')
    return render('login.html', context_instance=RequestContext(request))