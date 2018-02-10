import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','proTwo.settings')

import django
django.setup()

##fake data maker

import random
from proTwo_app.models import User
from faker import Faker

fakegen = Faker()

def populate(N=5):

    for users in range(N):
        fake_first_name = fakegen.name()
        fake_last_name  = fakegen.name()
        fake_email      = fakegen.email()

        users = User.objects.get_or_create(first_name=fake_first_name,last_name=fake_last_name,email=fake_email)


if __name__ == '__main__':
    print("populate script init")
    populate(20)
    print("populate script is compelete")
