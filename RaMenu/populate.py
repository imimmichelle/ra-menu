import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'RaMenu.settings')

import django
django.setup()

from desire_app.models import Desire, Category

def add_category(category):
    cat = Category.objects.get_or_create(category_name=category)[0]
    cat.save()
    return cat

def add_desire(desire, category):
    des = Desire.objects.get_or_create(desire_name=desire, category=category)[0]
    des.save()
    return des

file_name = input('Please enter file name:')
f = open(file_name, 'r')
lines = f.readlines()
for line in lines:
    # if it's a new category
    if (line.startswith('category')):
        line = line.replace("category:", '')
        category = line.strip()
        current_cat = add_category(category)
    # if it's a desire
    elif (len(line.strip()) != 0):
        desire = line.strip()
        add_desire(desire, current_cat)    
f.close()


