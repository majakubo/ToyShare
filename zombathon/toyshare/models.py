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
    rank = models.DecimalField(max_digits=2, decimal_places=1, blank=True)
    age = models.DecimalField(max_digits=2, decimal_places=0, blank=True)
    login = models.CharField(max_length=30, blank=True)
    transactions_quantity = models.DecimalField(max_digits=5, decimal_places=0, blank=True)

    def __str__(self):
        return self.login


class Toy(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=250)
    photo_path = models.TextField(max_length=100)
    condition = models.DecimalField(max_digits=2, decimal_places=0)
    age = models.DecimalField(max_digits=3, decimal_places=0)
    players_quantity = models.DecimalField(max_digits=2, decimal_places=0)
    owner = models.ForeignKey('auth.User', related_name='toys', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super(Toy, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Renting(models.Model):
    begin_date = models.DateField()
    end_date = models.DateField(blank=True)
    first_toy_id_ref = models.ForeignKey(Toy, related_name="first_toy", on_delete=models.PROTECT)
    second_toy_id_ref = models.ForeignKey(Toy, related_name="second_toy", on_delete=models.PROTECT)
    owner_id_ref = models.ForeignKey(ExtUser, on_delete=models.PROTECT, related_name="owner_id")
    user_id_ref = models.ForeignKey(ExtUser, on_delete=models.PROTECT, related_name="user_id")

    def __str__(self):
        return str(self.begin_date)+" "+self.owner_id_ref.login+"-"+self.user_id_ref.login


class Rate(models.Model):
    value = models.DecimalField(max_digits=2, decimal_places=0)
    message = models.TextField(max_length=500)
    toy_condition = models.DecimalField(max_digits=2, decimal_places=0)
    renting_id_ref = models.ForeignKey(Renting, on_delete=models.PROTECT)
    user_id_ref = models.ForeignKey(ExtUser, on_delete=models.PROTECT)

    def __str__(self):
        return self.renting_id_ref.login+" - "+self.user_id_ref.login


class Wanted(models.Model):
    user_id_ref = models.ForeignKey(ExtUser, on_delete=models.PROTECT)
    toy_id_ref = models.ForeignKey(Toy, on_delete=models.PROTECT)

    def __str__(self):
        return self.user_id_ref.login+" wants "+self.toy_id_ref.name


class Unwanted(models.Model):
    user_id_ref = models.ForeignKey(ExtUser, on_delete=models.PROTECT)
    toy_id_ref = models.ForeignKey(Toy, on_delete=models.PROTECT)

    def __str__(self):
        return self.user_id_ref.login+" unwanted "+self.toy_id_ref.name
