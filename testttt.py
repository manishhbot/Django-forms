import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','nyfirst.settings')

import django
django.setup()

import random
from my_first_1.models import Freedemo, Onboarded, Registrations
from faker import Faker

fakegen = Faker()

def populate(N=5):
    for i in range(N):
        num = 1
        fake_name = fakegen.name()
        fake_phone = fakegen.phone_number()
        fake_email = fakegen.email()
        fake_address = fakegen.address()
        fake_job = fakegen.job()
        fake_time = fakegen.time()

        var1 = Freedemo.objects.get_or_create(name=fake_name, phone = fake_phone, email = fake_email, address = fake_address)[0]

        var2 = Registrations.objects.get_or_create(name=var1, job=fake_job)[0]

        var3 = Onboarded.objects.get_or_create(name = var2, time=fake_time)[0]

if __name__ == "__main__":
    print("populating scripts")
    populate(20)
    print("populating complete")


        


