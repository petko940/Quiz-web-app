from django.urls import path, include
from apps.users.views import (RegisterView,
                              SignInView,
                              Logout)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', SignInView.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('auth/', include('social_django.urls', namespace='social')),
]
