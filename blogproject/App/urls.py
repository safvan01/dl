from .import views
from django.urls import path
from .views import post

urlpatterns = [
    # path('',views.PostList.as_view(), name="home"),
    path('<slug:slug>/',views.PostList.as_view(), name='post_detail'),
    path('',post)
]