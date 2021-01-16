from django.shortcuts import render,redirect
from .forms import UserCreationForm, LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from blog.models import post
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
            return redirect('home')

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
            return redirect('home')
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


def profile(request):
    posts =post.objects.filter(author=request.user)
    return render(request, 'user/profile.html', {
        'title':'الملف الشخصي',
        'posts':posts,
    })