# Generated by Django 3.2.7 on 2021-11-08 00:14

from django.db import migrations
from django.contrib.auth.models import User
from puttputt.models import *

def add_more_info(apps, scheme_editor):
    # get the models
    Profile = apps.get_model('puttputt', 'Profile')
    SponsorInfo = apps.get_model('puttputt', 'SponsorInfo')
    Tournament = apps.get_model('puttputt', 'Tournament')
    PlayerInfo = apps.get_model('puttputt', 'PlayerInfo')
    ManagerInfo = apps.get_model('puttputt', 'ManagerInfo')
    DrinkInfo = apps.get_model('puttputt', 'DrinkInfo')
    LeaderBoard = apps.get_model('puttputt', 'LeaderBoard')
    Prizes = apps.get_model('puttputt', 'Prizes')
    DrinkOrder = apps.get_model('puttputt', 'DrinkOrder')
    VenueInfo = apps.get_model('puttputt', 'VenueInfo')

    original_sponsor = None
    sponsor_info = None

    # SECTION FOR CREATING THE ORIGINAL SPONSOR
    try: 
        original_sponsor = User.objects.get(username='sponsor')
        sponsor_profile = Profile.objects.get(user_id = original_sponsor.id)
        sponsor_info = SponsorInfo.objects.get(profile=sponsor_profile)
    except:
        original_sponsor = User.objects.create_user(username='sponsor', password='sponsor')
        original_sponsor = User.objects.get(username='sponsor')

        sponsor_profile = Profile(user_id = original_sponsor.id, profile_type='SPO')
        sponsor_profile.save()

        sponsor_info = SponsorInfo(profile=sponsor_profile, title='The Original Sponsor')
        sponsor_info.save()

    # VENUE INFO -- *IMPORTANT* -- THERE SHOULD ONLY EVER BE ONE RECORD IN THIS TABLE!
    try: 
        venue = VenueInfo.objects.all()[:1].get()
    except:
        venue = VenueInfo.objects.create(title='PuttPutt Golf', number_of_holes=10)
        venue.save()

    # THE ORIGINAL DRINKS
    try:
        water = DrinkInfo.objects.get(title='water') 
        coffee = DrinkInfo.objects.get(title='cofee')
        milk = DrinkInfo.objects.get(title='milk')
        vodka = DrinkInfo.objects.get(title='vodka')
    except:
        water = DrinkInfo.objects.create(title='water', price=3)
        water.save()

        coffee = DrinkInfo.objects.create(title='coffee', price=4)
        coffee.save()

        milk = DrinkInfo.objects.create(title='milk', price=5)
        milk.save()

        vodka = DrinkInfo.objects.create(title='vodka', price=7)
        vodka.save()

    # TODO: add an original barista so we don't have to...
    try: 
        barista = User.objects.get(username='barista')
    except:
        barista = User.objects.create_user(username='barista', password='barista')
        barista_profile = Profile(user_id = barista.id, profile_type='BAR')
        barista_profile.save()

class Migration(migrations.Migration):

    dependencies = [
        ('puttputt', '0006_auto_20211107_2341'),
    ]

    operations = [
        migrations.RunPython(add_more_info)
    ]
