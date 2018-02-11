from django.urls import path

from posts.views import HomePage, LatestWhispers, PopularWhispers, WhisperDetail, CreateWhisper, UpdateWhisper, \
    DeleteWhisper, UpdateProfile, like_whisper_list, like_whisper_detail

app_name='posts'

urlpatterns=[
    path('', HomePage.as_view(), name='home'),
    path('latest/', LatestWhispers.as_view(), name='latest'),
    path('popular/', PopularWhispers.as_view(), name='popular'),
    path('story/<int:pk>/', WhisperDetail.as_view(), name='whisper-detail'),
    path('story/create/', CreateWhisper.as_view(), name='create-whisper'),
    path('story/<int:pk>/update/', UpdateWhisper.as_view(), name='update-whisper'),
    path('story/<int:pk>/like/', like_whisper_list, name='like-whisper-list'),
    path('story/<int:pk>/like/d/', like_whisper_detail, name='like-whisper-detail'),
    path('story/<int:pk>/delete/', DeleteWhisper.as_view(), name='delete-whisper'),
    path('profile/<int:pk>/update/', UpdateProfile.as_view(), name='update-profile'),
]