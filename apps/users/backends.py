from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class CustomAuthenticationBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        if username is None:
            return None

        try:
            user = UserModel.objects.get(username=username)
        except UserModel.DoesNotExist:
            try:
                user = UserModel.objects.get(email=username.lower())
            except UserModel.DoesNotExist:
                return None

        if user.check_password(password):
            return user

    def get_user(self, user_id):
        try:
            return UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None
