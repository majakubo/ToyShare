# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class ExtUser(models.Model):
    userbase = models.OneToOneField(User, on_delete=models.CASCADE)
    tel = models.CharField(max_length=12, blank=True)
    city = models.CharField(max_length=30, blank=True)
    street = models.CharField(max_length=30, blank=True)
    house_number = models.CharField(max_length=10, blank=True)
    post_code = models.CharField(max_length=6, blank=True)
    age = models.DecimalField(max_digits=2, decimal_places=0, blank=True)
    login = models.CharField(max_length=30, blank=True)
    transactions_quantity = models.DecimalField(max_digits=5, decimal_places=0, blank=True)


class Toy(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=250)
    photo_path = models.TextField(max_length=100)
    condition = models.DecimalField(max_digits=2, decimal_places=0)
    age = models.DecimalField(max_digits=3, decimal_places=0)
    players_quantity = models.DecimalField(max_digits=2, decimal_places=0)
    owner = models.ForeignKey('auth.User', related_name='toy_owner', on_delete=models.CASCADE)


class Renting(models.Model):
    begin_date = models.DateField()
    end_date = models.DateField()
    toy_id_ref = models.ForeignKey(Toy, on_delete=models.PROTECT)
    owner_id_ref = models.ForeignKey(ExtUser, on_delete=models.PROTECT, related_name="owner_id")
    user_id_ref = models.ForeignKey(ExtUser, on_delete=models.PROTECT, related_name="user_id")


class Rate(models.Model):
    value = models.DecimalField(max_digits=2, decimal_places=0)
    message = models.TextField(max_length=500)
    toy_condition = models.DecimalField(max_digits=2, decimal_places=0)
    renting_id_ref = models.ForeignKey(Renting, on_delete=models.PROTECT)
    user_id_ref = models.ForeignKey(ExtUser, on_delete=models.PROTECT)


class Wants(models.Model):
    user_id_ref = models.ForeignKey(ExtUser, on_delete=models.PROTECT)
    toy_id_ref = models.ForeignKey(Toy, on_delete=models.PROTECT)

class Unwanted(models.Model):
    user_id_ref = models.ForeignKey(ExtUser, on_delete=models.PROTECT)
    toy_id_ref = models.ForeignKey(Toy, on_delete=models.PROTECT)
