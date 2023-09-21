from django.shortcuts import render
from .models import Post
from django.views import generic
# Create your views here.


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'base.html'

class DetailView(generic.DetailView):
    model = Post
    template_name = 'base.html'

def post(request):
    from django.db import connection
    context = {'rows': []}
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM App_post")
        context.rows = cursor.fetchall()
    # post = 
    return render(request,'base.html', context)