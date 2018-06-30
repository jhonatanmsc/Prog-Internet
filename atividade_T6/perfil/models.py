from django.db import models
from django.contrib.auth.models import (AbstractUser,
                                        UserManager)


class User(AbstractUser):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.username

    @classmethod
    def save_from_json(cls, id, name, email, address, *args, **kwargs):
        return cls.objects.create(pk=id, username=name, email=email, address=Address.save_from_json(**address))



class Character(models.Model):
    name = models.CharField(max_length=100)
    race = models.ForeignKey('Races', related_name='characters', on_delete=models.CASCADE)
    characterType = models.ForeignKey('CharacterType', related_name='characters', on_delete=models.CASCADE)
    native = models.ForeignKey('Area', related_name='habitants', on_delete=models.CASCADE)
    musicTheme = models.ForeignKey('Music', related_name='characters', on_delete=models.CASCADE)


class Item(models.Model):
    name = models.CharField(max_length=100)
    itemClass = models.ForeignKey('ItemClass', related_name='itens', on_delete=models.CASCADE)
    effect = models.CharField(max_length=300)
    patter = models.CharField(max_length=100)
    location = models.ForeignKey('Area', related_name='itens', on_delete=models.CASCADE)
    cost = models.IntegerField()


class ItemClass(models.Model): 
    name = models.CharField(max_length=100)


class Area(models.Model):
    name = models.CharField(max_length=100)
    musicTheme = models.ForeignKey('Music', related_name='areas', on_delete=models.CASCADE)


class Race(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)


class CharacterType(models.Model):
    name = models.CharField(max_length=100)


class Music(models.Model):
    name = models.CharField(max_length=100)