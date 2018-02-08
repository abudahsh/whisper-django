from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.views.generic.edit import ModelFormMixin, UpdateView, DeleteView

from posts.models import Whisper

class WhisperOwnerPermissionMixin(UserPassesTestMixin):
    # Check if the current user is the same as the whisper.creator to allow to edit the form
    def test_func(self):
        # only current user and staff users are allowed to edit the whisper
        return self.request.user.profile == self.get_object().creator or self.request.user.is_staff


class HomePage (TemplateView):
    template_name = 'home.html'



class LatestWhispers(ListView):
    model = Whisper
    template_name = 'whisper_list.html'
    context_object_name = 'whispers'


class PopularWhispers(ListView):
    """ ordering the whisper by likes and only few number only 10 stories for now """
    queryset = Whisper.objects.order_by('-likes')[:10]
    template_name = 'whisper_list.html'
    context_object_name = 'whispers'


class WhisperDetail(DetailView):
    """ Detail View of whisper where you can find the profile info of the whisper owner, and the comments on it"""
    model = Whisper
    template_name = 'whisper_detail.html'
    context_object_name = 'whisper'


class CreateWhisper(CreateView):
    model = Whisper
    fields = ['text', 'image']
    template_name = 'create_whisper.html'
    success_url = reverse_lazy('posts:latest') #redirect to latest stories view

    def form_valid(self, form):
        form.instance.creator=self.request.user.profile #takes the current user as the creator of the whisper
        return super().form_valid(form)


class UpdateWhisper(WhisperOwnerPermissionMixin,UpdateView):
    model = Whisper
    fields = ['text', 'image']
    template_name = 'create_whisper.html'
    success_url = reverse_lazy('posts:latest')
    redirect_field_name = reverse_lazy('posts:latest')



    def form_valid(self, form):
        form.instance.creator=self.request.user.profile #takes the current user as the creator of the whisper
        return super().form_valid(form)


class DeleteWhisper(WhisperOwnerPermissionMixin,DeleteView):
    model = Whisper
    success_url = reverse_lazy('posts:latest')
    template_name = 'whisper_confirm_delete.html'