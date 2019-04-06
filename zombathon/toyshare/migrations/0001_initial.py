# Generated by Django 2.2 on 2019-04-06 14:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tel', models.CharField(blank=True, max_length=12)),
                ('city', models.CharField(blank=True, max_length=30)),
                ('street', models.CharField(blank=True, max_length=30)),
                ('house_number', models.CharField(blank=True, max_length=10)),
                ('post_code', models.CharField(blank=True, max_length=6)),
                ('rank', models.DecimalField(blank=True, decimal_places=1, max_digits=2)),
                ('age', models.DecimalField(blank=True, decimal_places=0, max_digits=2)),
                ('login', models.CharField(blank=True, max_length=30)),
                ('transactions_quantity', models.DecimalField(blank=True, decimal_places=0, max_digits=5)),
                ('userbase', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Toy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(max_length=250)),
                ('photo_path', models.TextField(max_length=10000)),
                ('condition', models.DecimalField(decimal_places=0, max_digits=2)),
                ('age', models.DecimalField(decimal_places=0, max_digits=3)),
                ('players_quantity', models.DecimalField(decimal_places=0, max_digits=2)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='toys', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Wanted',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('toy_id_ref', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='toyshare.Toy')),
                ('user_id_ref', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='toyshare.ExtUser')),
            ],
        ),
        migrations.CreateModel(
            name='Unwanted',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('toy_id_ref', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='toyshare.Toy')),
                ('user_id_ref', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='toyshare.ExtUser')),
            ],
        ),
        migrations.CreateModel(
            name='Renting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('begin_date', models.DateField()),
                ('end_date', models.DateField(blank=True)),
                ('first_toy_id_ref', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='first_toy', to='toyshare.Toy')),
                ('owner_id_ref', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='owner_id', to='toyshare.ExtUser')),
                ('second_toy_id_ref', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='second_toy', to='toyshare.Toy')),
                ('user_id_ref', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='user_id', to='toyshare.ExtUser')),
            ],
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.DecimalField(decimal_places=0, max_digits=2)),
                ('message', models.TextField(max_length=500)),
                ('toy_condition', models.DecimalField(decimal_places=0, max_digits=2)),
                ('renting_id_ref', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='toyshare.Renting')),
                ('user_id_ref', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='toyshare.ExtUser')),
            ],
        ),
    ]
