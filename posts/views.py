from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, RedirectView
from django.views.generic.edit import ModelFormMixin, UpdateView, DeleteView

from accounts.models import Profile
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
    ordering = '-time_stamp'

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
        form.instance.image = self.request.FILES['image']
        return super().form_valid(form)


class UpdateWhisper(WhisperOwnerPermissionMixin,UpdateView):
    model = Whisper
    fields = ['text', 'image']
    template_name = 'update_whisper.html'
    success_url = reverse_lazy('posts:latest')
    redirect_field_name = reverse_lazy('posts:latest')



    def form_valid(self, form):
        form.instance.creator=self.request.user.profile #takes the current user as the creator of the whisper
        form.instance.image = self.request.FILES['image']
        return super().form_valid(form)


class DeleteWhisper(WhisperOwnerPermissionMixin,DeleteView):
    model = Whisper
    success_url = reverse_lazy('posts:latest')
    template_name = 'whisper_confirm_delete.html'


class UpdateProfile(LoginRequiredMixin, UpdateView):
    model = Profile
    fields = ['nickname', 'age', 'location']
    success_url = reverse_lazy('posts:latest')
    template_name = 'update_profile.html'





def like_whisper_list(request, pk):
    whisper=get_object_or_404(Whisper, pk=pk)
    try:
        if whisper.is_liked:
            whisper.is_liked= False
            whisper.likes-=1
        else:
            whisper.likes+=1
            whisper.is_liked=True
        whisper.save()
    except (KeyError, Whisper.DoesNotExist):
        return HttpResponse(404)
    else:
        return redirect(reverse_lazy('posts:latest'))



def like_whisper_detail(request, pk):
    whisper=get_object_or_404(Whisper, pk=pk)
    try:
        if whisper.is_liked:
            whisper.is_liked= False
            whisper.likes-=1
        else:
            whisper.likes+=1
            whisper.is_liked=True
        whisper.save()
    except (KeyError, Whisper.DoesNotExist):
        return HttpResponse(404)
    else:
        return redirect(reverse_lazy('posts:whisper-detail', kwargs={'pk':pk}))
