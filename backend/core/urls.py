from django.urls import path
from core.views import (
    JoinMatchView
)


urlpatterns = [
    path(
        'join-match/', JoinMatchView.as_view(),
        name='join-match'
    ),
]
