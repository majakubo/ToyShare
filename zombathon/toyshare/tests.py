from django.test import TestCase
from .models import ExtUser, Toy, Renting, Rate, Wants
from django.contrib.auth.models import User
import io

from toyshare.serializers import UserSerializer, ExtUserRegisterSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

def create_user(phone='7244427575', user_n='majaku'):
    u = User(username=user_n, password='123')
    u.save()
    e = ExtUser(userbase=u,
                tel=phone,
                city='Kolobrzeg',
                street='Knierskiego',
                house_number='12',
                post_code='78-100',
                age=12.0,
                login='majaku',
                transactions_quantity=12
                )
    return e


def create_toy(user, name='Klocki lego'):
    t = Toy(name=name,
            description="Fajny zestaw klocków",
            photo_path="data/zdj1.jpg",
            condition="5",
            age=7,
            players_quantity=1,
            user_id_ref=user)
    return t


class ExtUserTests(TestCase):

    def test_creating_extuser(TestCase):
        eu = create_user()
        eu.save()
        print(1, eu.tel)

    def test_creating_toy(TestCase):
        eu = create_user()
        eu.save()

        t = create_toy(eu, 'Samochodzik')
        t.save()
        print(2, t.user_id_ref)

    def test_creating_renting(TestCase):
        lend = create_user(phone='111111111111')
        lend.save()
        provide = create_user(phone='222222222222', user_n='szymek')
        provide.save()

        t = create_toy(provide, 'Autko')
        t.save()

        re = Renting(begin_date='2000-01-01',
                          end_date='1999-12-12',
                          toy_id_ref=t,
                          owner_id_ref=lend,
                          user_id_ref=provide)
        re.save()

        print(3,re.toy_id_ref.name,
              re.owner_id_ref.tel,
              re.user_id_ref.tel)

    def test_creating_rate(TestCase):
        u = create_user('123456789')
        u.save()

        provide = create_user(phone='222222222222', user_n='jaaa')
        provide.save()

        t = create_toy(provide, 'Autko')
        t.save()

        renting = Renting(begin_date='2000-01-01',
                          end_date='1999-12-12',
                          toy_id_ref=t,
                          owner_id_ref=u,
                          user_id_ref=provide)
        renting.save()

        r = Rate(value=5,
                 message="Zajebisty deal",
                 toy_condition=10,
                 renting_id_ref=renting,
                 user_id_ref=u)
        r.save()
        print(4,r.renting_id_ref.toy_id_ref.name)

    def test_creating_wants(TestCase):
        u = create_user(phone='222222222222')
        u.save()

        t = create_toy(u, 'Autko')
        t.save()

        w = Wants(user_id_ref=u,
                  toy_id_ref=t)

        print(5, w.user_id_ref.tel)


# Create your tests here


class SerializableTest(TestCase):
    def test_no_1(TestCase):
        u = create_user()
        u.save()

        serializer = ExtUserRegisterSerializer(u)
        #content = JSONRenderer().render(serializer.data)
        print(serializer.data)
        #stream = io.BytesIO(content)
        #data = JSONParser().parse(stream)

        #print(data)

