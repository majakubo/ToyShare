from django.test import TestCase
from .models import ExtUser
from django.contrib.auth.models import User

class ExtUserTests(TestCase):
    def test_creating_extuser(TestCase):
        u = User(username='majaku', password='123')
        u.save()
        e = ExtUser(userbase=u,
                    tel='7244427575',
                    city='Kolobrzeg',
                    street='Knierskiego',
                    house_number='12',
                    post_code='78-100',
                    age=12.0,
                    login='majaku',
                    transactions_quantity=12

        )
        e.save()
        print(e.tel)

# Create your tests here.
