from mongoengine import Document
from mongoengine.fields import EmailField, StringField, ImageField, BooleanField
from mongoengine.errors import DoesNotExist


class Account(Document):
    email = EmailField(required=True, unique=True)
    password = StringField(min_length=8, max_length=20, required=True)
    first_name = StringField(min_length=3, max_length=50)
    second_name = StringField(min_length=3, max_length=50)
    avatar = ImageField(size=(75, 75, True), thumbnail_size=(50, 50, True), collection_name="avatar")
    is_active = BooleanField(default=True)
    is_staff = BooleanField(default=True)
    is_superuser = BooleanField(default=False)

    def __str__(self):
        return self.email

    # def get_full_name(self):
    #     return "%s %s" % (self.first_name, self.second_name)

    def create_user(self, email, password1, password2, **kwargs):
        if password1 != password2:
            return {"status": "Error", "details": "Password is not match!"}
        try:
            Account.objects(email=email)
        except DoesNotExist:
            user = Account(email=email, password=password1)
            user.first_name = kwargs['first_name']
            user.second_nane = kwargs['second_name']
            self.update_avatar(self, user, kwargs['avatar'])


        user = super(Account, self).save()
        return user

    def create_super_user(self):
        user = self.create_user()
        user.is_superuser = True
        user.is_active = True
        user.save()
        return user

    def update_avatar(self, user=None, avatar):
        if user is not None:

            file = open("avatar_%s" % self.email, 'wb')
            file.write(avatar)
            self.avatar.save(file)
            file.close()
            user = super(Account, self).save()
            return user
