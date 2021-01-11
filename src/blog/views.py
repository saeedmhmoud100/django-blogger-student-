from django.shortcuts import render, get_object_or_404
from .models import post,comment
from .form import NewComment

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
    comments = posts.comments.filter(active=True) #comment.objects.all().filter(active=True, Post=posts)
    comment_form = NewComment()
    #comment_form = None
    context = {
        'title':posts,
        'post':posts,
        'comments':comments,
        'comment_form':comment_form
    }

    if request.method == "POST":
        comment_form = NewComment(data=request.POST)
        if comment_form.is_valid():
            print('yes')
            new_comment = comment_form.save(commit=False)
            new_comment.Post=posts
            new_comment.save()
            comment_form = NewComment()
            
    else:
        comment_form = NewComment()
    return render(request, 'blog/detail.html', context)