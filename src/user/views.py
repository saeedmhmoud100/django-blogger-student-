from django.shortcuts import render,redirect
from .forms import UserCreationForm, LoginForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from blog.models import post
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            user =form.save(commit=False)
            user.set_password(password)
            user.save()
            username = form.cleaned_data['username']
            messages.success(request,f'تهانينا {username} لقد تم التسجيل بنجاح.')
            return redirect('login')

    else:
        form = UserCreationForm()
    return render(request, 'user/register.html', {
        'title': 'التسجيل',
        'form': form
    })

def Login_user(request):
    if request.method =='POST':
        form = LoginForm()
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            messages.warning(request, 'هناك خطأ في اسم المستخدم او كلمة المرور')
            print('no')
    else:
        form = LoginForm()
    return render(request, 'user/login.html', {
        'title':'تسجيل الدخول',
        'form': form
    })


def Logout_user(request):
    logout(request)
    return render(request, 'user/logout.html', {
        'title': 'تسجيل الخروج',

    })

@login_required(login_url='login')
def profile(request):
    posts =post.objects.filter(author=request.user)
    posts_list =post.objects.filter(author=request.user)
    paginator = Paginator(posts_list, 10)
    page = request.GET.get('page')
    try:
        posts_list= paginator.page(page)
    except PageNotAnInteger:
        posts_list= paginator.page(1)
    except EmptyPage:
        posts_list= paginator.page(paginator.num_page)
    
    return render(request, 'user/profile.html', {
        'title':'الملف الشخصي',
        'posts':posts,
        'page':page,
        'posts_list':posts_list
    })


@login_required(login_url='login')
def profile_update(request):
    if request.method== 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES ,instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request,'تم تحديث الملف الشخصي')
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
    context= {
        'title':'تعديل الملف الشخصي',
        'user_form':user_form,
        'profile_form':profile_form,
        }

    return render(request, 'user/profile_update.html', context)