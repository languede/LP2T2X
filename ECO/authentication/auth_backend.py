from django.contrib.auth.backends import ModelBackend
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()


class PasswordlessAuthBackend(ModelBackend):
    """
    Authenticate against the settings ADMIN_LOGIN and ADMIN_PASSWORD.

    Use the login name and a hash of the password. For example:

    ADMIN_LOGIN = 'admin'
    ADMIN_PASSWORD = 'pbkdf2_sha256$30000$Vo0VlMnkR4Bk$qEvtdyZRWTcOsCnI/oQ7fVOu1XAURIZYoOZ3iq8Dr4M='
    """ ""

    def authenticate(self, request=None, **kwargs):
        try:
            if request.path_info != "/checkout/":
                return None
            return User.objects.get(phone_number=kwargs["phone_number"])
        except User.DoesNotExist:
            return None

    # def get_user(self, user_id):
    #     try:
    #         return User.objects.get(pk=user_id)
    #     except User.DoesNotExist:
    #         return None
