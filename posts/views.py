from django.views.generic import ListView
from .models import Post

class HomePageView(ListView):
    '''This contains the data to be displayed on the home page'''
    model = Post
    template_name = 'home.html'
    context_object_name = 'all_posts_list'
