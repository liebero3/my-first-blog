#def homepage(request):
#    if request.user.is_anonymous():
#
#    else:


from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.http import *
from django.shortcuts import redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout, views
from django.shortcuts import render, get_object_or_404
from .forms import CommentForm
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import Group, User

# Create your views here.
@user_passes_test(lambda u: Group.objects.get(name='EFGK2PH1617') in u.groups.all(), login_url='/login/')
#@login_required(login_url='/login/')
def post_list(request):
    posts = Post.objects.filter(kurs__name='EFGK2PH1617').filter(pdate__lte=timezone.now())#.order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

@user_passes_test(lambda u: Group.objects.get(name='8aPH1617') in u.groups.all(), login_url='/login/')
#@login_required(login_url='/login/')
def post_list8a(request):
    posts = Post.objects.filter(kurs__name='8aPH1617').filter(pdate__lte=timezone.now())#.order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

@user_passes_test(lambda u: Group.objects.get(name='8bPH1617') in u.groups.all(), login_url='/login/')
#@login_required(login_url='/login/')
def post_list8b(request):
    posts = Post.objects.filter(kurs__name='8bPH1617').filter(pdate__lte=timezone.now())#.order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

@user_passes_test(lambda u: Group.objects.get(name='9cM1617') in u.groups.all(), login_url='/login/')
#@login_required(login_url='/login/')
def post_list9c(request):
    posts = Post.objects.filter(kurs__name='9cM1617').filter(pdate__lte=timezone.now())#.order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

@login_required(login_url='/login/')
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

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
            login(request, user)
            return HttpResponseRedirect('/')
    return render(request, 'blog/login.html')

def change_password(request):
    password_old = password_new1 = password_new2 = ''
    if request.user.is_authenticated():
        if request.POST:
            password_old = request.POST['password_old']
            password_new1 = request.POST['password_new1']
            password_new2 = request.POST['password_new2']

            if request.user.check_password(password_old) and password_new1 == password_new2:
                request.user.set_password(password_new1)
                request.user.save()
                return render(request, 'blog/change_password_done.html')
            else:
                return render(request, 'blog/change_password.html')
        else:
            return render(request, 'blog/change_password.html')
    else:
        return render(request, 'blog/login.html')

def change_password_done(request):
    return render(request, 'blog/change_password_done.html')

@login_required(login_url='/login/')
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('blog:post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})