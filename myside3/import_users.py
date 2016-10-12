#-*- coding: UTF-8 -*-
from django.contrib.auth.models import User

def Create_User(vorname, nachname):
    user = User.objects.create_user('{}.{}'.format(vorname.nachname), password='{}.{}'.format(nachname.vorname))
    user.is_superuser = False
    user.is_staff = False
    user.save()

def Read_List(textdatei):
    with open(textdatei, 'r') as namensliste:
        vorname = []
        nachname = []
        for name in namensliste:
            vorname.append(name.strip('\n').replace(" ", "_").split(';')[0])
            nachname.append(name.strip('\n').replace(" ", "_").split(';')[1])
    # with open('klasse2.csv', 'w') as machmal:
    #     for i in range(0,len(vorname)):
    #         machmal.write('{},{}{}'.format(nachname[i], vorname[i], '\n'))

Read_List('') #hier die Textdatei einfuegen
for i in range(0, len(vorname)):
    Create_User(vorname[i], nachname[i])