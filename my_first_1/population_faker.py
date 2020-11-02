import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','nyfirst.settings')

import django
django.setup()

import random
from my_first_1.models import Freedemo, Onboarded, Registrations
from faker import Faker

fakegen = Faker()
Details = ['name','phone number', 'email']

def add_details():
    A = Freedemo.objects.get_or_create(name=random.choice(Details))[0]
    A.save()
    return A

def populate(N=5):
    for i in range(N):
        i_name = add_details()

        fake_phone = fakegen.phone()
        fake_email = fakegen.email()
        fake_occupation = fakegen.company()
        fake_course = fakegen.book()
        fake_time = fakegen.time()

        Fredmo = Freedemo.objects.get_or_create(name=i_name, phone = fake_phone, email = fake_email, occupation = fake_occupation)[0]

        rgtr = Registrations.objects.get_or_create(name=i_name, course=fake_course)[0]

        onnbrd = Onboarded.objects.get_or_create(name = rgtr, time=fake_time)[0]

if __name__ == "__main__":
    print("populating scripts")
    populate(20)
    print("populating complete")


        


