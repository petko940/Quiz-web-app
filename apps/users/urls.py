from django.urls import path, include
from apps.users.views import (RegisterView,
                              SignInView,
                              Logout,
                              ProfileView,
                              SettingProfileView,
                              ChangeUsernameView,
                              ChangeEmailView,
                              ChangePasswordView,
                              DeleteProfileView
                              )

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', SignInView.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('auth/', include('social_django.urls', namespace='social')),

    path('profile/<str:username>/', include([
        path('', ProfileView.as_view(), name='profile'),
        path('settings/', SettingProfileView.as_view(), name='settings'),
        path('change-username/', ChangeUsernameView.as_view(), name='change_username'),
        path('change-email/', ChangeEmailView.as_view(), name='change_email'),
        path('change-password/', ChangePasswordView.as_view(), name='change_password'),
        path('delete-profile/', DeleteProfileView.as_view(), name='delete_profile'),
    ])),

]
