from json import loads

from django.contrib.auth.decorators import login_required
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse, HttpResponseBadRequest
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.generic import ListView, DetailView, View, CreateView
from django.forms import Form

from .forms import CommentForm
from .models import Post


@method_decorator(never_cache, name='dispatch')
class BlogView(ListView):
    template_name = "blog.html"
    model = Post


@method_decorator(never_cache, name='dispatch')
class PostView(DetailView):
    template_name = 'post.html'
    model = Post


@method_decorator(login_required, name='dispatch')
class UserPostView(View):
    form_class: type[Form]

    def post(self, req: WSGIRequest):
        data = loads(req.body)
        form = self.form_class(data=data)
        form.is_valid()
        if len(form.errors) != 0:
            return HttpResponseBadRequest(form.errors)
        form.save()
        return HttpResponse("created!")



class CommentCreateView(UserPostView):
    form_class = CommentForm
