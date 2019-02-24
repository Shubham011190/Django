import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ProTwo.settings')

import django
django.setup()

from AppTwo.models import User
from faker import Faker

fakegen = Faker()

def populate(N=5):

    for entry in range(N):

        fakeName=fakegen.name().split()
        fakeFirstName = fakeName[0]
        fakeLastName = fakeName[1]
        fakeEmail = fakegen.email()

        user = User.objects.get_or_create(firstName = fakeFirstName, lastName = fakeLastName, email = fakeEmail)[0]


if __name__ == '__main__':
    print('Populating Scripts!')
    populate(20)
    print('Population Complete!')
