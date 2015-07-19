from django.contrib.auth import get_user_model as get_django_user_model


class UserService(object):
    def get_user_model(self):
        return get_django_user_model()

    def create_new_user(self, username, email, password):
        _User = self.get_user_model()
        new_user = _User.objects.create(username=username, email=email)
        new_user.set_password(password)
        new_user.is_active = True
        new_user.save()
        return new_user

    def get_user(self, pk):
        _User = self.get_user_model()
        return _User.objects.get(pk=pk)
