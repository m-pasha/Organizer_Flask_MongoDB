from mongoengine import Document
from mongoengine.fields import EmailField, StringField, ImageField


class ManagerAccount(Document):

    def create_user(self, email, password, first_name):
        if email is None:
            raise TypeError("User must have email!")
        if password is None:
            raise TypeError("User must have password!")
        if first_name is None:
            raise TypeError("User must have first name!")
        user = self.objects(email=email, password=password, first_name=first_name)
        user.save()
        return user

    def create_super_user(self):
        user = self.create_user(email, password, first_name)
        user.is_superuser = True
        user.is_active = True
        user.save()
        return user


class Account(Document):
    email = EmailField(required=True, unique=True)
    password = StringField(min_length=8, max_length=20, required=True)
    first_name = StringField(min_length=3, max_length=50, required=True)
    second_name = StringField(min_length=3, max_length=50)
    avatar = ImageField(size=(100, 100, True), thumbnail_size=(50, 50, True), collection_name="avatar")
    is_active = BooleanField(default=False)
    is_superuser = BooleanField(default=False)

    objects = ManagerAccount()

    def __str__(self):
        return self.email