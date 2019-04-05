# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class ExtUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tel = models.CharField(max_length=12)
    city = models.CharField(max_length=30)
    street = models.CharField(max_length=30)
    house_number = models.CharField(max_length=10)
    post_code = models.CharField(max_length=6)
    age = models.DecimalField()
    login = models.CharField(max_length=30)
    transactions_guantity = models.DecimalField()


class Toy(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=250)
    photo_path = models.TextField(max_length=100)
    condition = models.DecimalField()
    age = models.DecimalField()
    players_quantity = models.DecimalField()
    user_id_ref = models.ForeignKey(ExtUser, on_delete=models.CASCADE)

class Renting(models.Model):
    begin_date = models.DateField()
    end_date = models.DateField()
    toy_id_ref = models.ForeignKey(Toy, on_delete=models.PROTECT,
                                   related_name='toy_id_ref')
    owner_id_ref = models.ForeignKey(ExtUser, on_delete=models.PROTECT,
                                    related_name='owner_id_ref')
    user_id_ref = models.ForeignKey(ExtUser, on_delete=models.PROTECT,
                                    related_name='user_id_ref')


class Rate(models.Model):
    value = models.DecimalField()
    message = models.TextField(max_length=500)
    toy_condition = models.DecimalField()
    renting_id_ref = models.ForeignKey(Renting, on_delete=models.PROTECT,
                                       related_name='renting_id_ref')
    user_id_ref = models.ForeignKey(ExtUser, on_delete=models.PROTECT,
                                    related_name='user_id_ref')


class Wants(models.Model):
    user_id_ref = models.ForeignKey(ExtUser, on_delete=models.PROTECT,
                                    related_name='user_id_ref')
    toy_id_ref = models.ForeignKey(Toy, on_delete=models.PROTECT,
related_name='toy_id_ref')
