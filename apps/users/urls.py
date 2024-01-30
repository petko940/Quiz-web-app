from django.urls import path, include
from apps.users.views import (RegisterView,
                              SignInView,
                              Logout,
                              ProfileView,
                              SettingProfileView,
                              ChangeUsernameView,
                              )

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', SignInView.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('auth/', include('social_django.urls', namespace='social')),

    path('profile/<str:username>/', include([
        path('', ProfileView.as_view(), name='profile'),
        path('settings/', SettingProfileView.as_view(), name='settings'),
        path('change_username/', ChangeUsernameView.as_view(), name='change_username'),
    ])),

]
