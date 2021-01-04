from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView
from .forms import AddPost
from .models import Article
from django.shortcuts import render



def wrapper(fn):
    """wrapper function for simple functions"""

    def get(request, *args, **kwargs):
        news = Article.objects.all()
        return render(request, fn(*args, **kwargs), {'alln': news})

    return get


class ArticleCreate(LoginRequiredMixin, CreateView):
    """view for creating article"""
    model = Article
    template_name = 'create_change.html'
    form_class = AddPost

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['available'] = Article.objects.filter(author=self.request.user).order_by('-date')
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)


class ArticleDelete(LoginRequiredMixin, DeleteView):
    """view for deleting article"""
    model = Article
    template_name = 'create_change.html'
    success_url = reverse_lazy('create')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.request.user != self.object.author:
            return self.handle_no_permission()
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)


class ArticleUpdate(LoginRequiredMixin, UpdateView):
    """view for updating of article"""
    model = Article
    template_name = 'create_change.html'
    success_url = reverse_lazy('create')
    form_class = AddPost

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if not self.request.user == kwargs['instance'].author:
            return self.handle_no_permission()
        return kwargs


