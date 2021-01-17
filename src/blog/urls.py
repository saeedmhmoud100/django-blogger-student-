from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path("about/", views.about, name="about"),
    path('detail/<int:post_id>', views.post_detail, name='detail'),
    path('new_post/',views.PostCreateViews.as_view(), name='new_post'),
    path('detail/<slug:pk>/update/', views.PostUpdateViews.as_view(), name='post-update'),
    path('detail/<slug:pk>/delete/', views.PostDeleteview.as_view(), name='post-delete'),

    ]
