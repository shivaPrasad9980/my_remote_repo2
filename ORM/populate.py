import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ORM.settings') # crudproject is your project name 
import django
django.setup()
import random
from testapp.models import Employee #this is application name and model
from faker import Faker
fake = Faker()


def populate(n):
  for i in range(n):
    feno = random.randint(100,999)
    fename = fake.name()
    fesal= random.randint(10000,20000)
    feadd = fake.city()
    employee = Employee.objects.get_or_create(eno = feno ,ename=fename, esal=fesal, eadd = feadd)

n = int(input("enter your no: "))

populate(n)