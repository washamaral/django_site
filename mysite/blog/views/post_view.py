from django.http import HttpResponse
from django.views import generic

class PostView(generic.DetailView):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Hello, world. This is my first django project.")
    # model = Post
    # template_name = 'blog/post.html'
    # context_object_name = 'post'