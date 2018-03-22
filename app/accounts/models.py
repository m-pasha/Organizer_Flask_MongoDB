class Account():
    email = EmailField(unique=True, required=True)
    name = StringField(min=3, max=20)