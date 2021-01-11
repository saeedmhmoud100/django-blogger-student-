from django.shortcuts import render, get_object_or_404
from .models import post,comment
# Create your views here.


posts =[
        {
        'title':'التدوينة الاولي',
        'content':'نص التدوينة الاولي كنص تجريبي',
        'post_date':'15-3-2020',
        'author':'Ahmed Mhmoud',
    },
        {
        'title':'التدوينة الثانية',
        'content':'نص التدوينة الثانية كنص تجريبي',
        'post_date':'15-3-2020',
        'author':'Ahmed Mhmoud',
    },
        {
        'title':'التدوينة الثالثة',
        'content':'نص التدوينة الثالثة كنص تجريبي',
        'post_date':'15-3-2020',
        'author':'Ahmed Mhmoud',
    },
        {
        'title':'التدوينة الرابعة',
        'content':'نص التدوينة الرابعة كنص تجريبي',
        'post_date':'15-3-2020',
        'author':'Ahmed Mhmoud',
    }]



def home(request):

    context ={
        'title':'الصفحة الرئيسية',
        'posts': post.objects.all(),
    }
    return render(request, 'blog/index.html',context)

def about(request):
    return render(request, 'blog/about.html', {'title':'من انا'})


def post_detail(request, post_id):

    posts= get_object_or_404(post, pk= post_id)
    comments = comment.objects.all().filter(active=True, Post=posts)
    context = {
        'title':posts,
        'post':posts,
        'comments':comments,
    }
    return render(request, 'blog/detail.html', context)