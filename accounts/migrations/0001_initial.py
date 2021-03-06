# Generated by Django 2.0.2 on 2018-02-04 13:50

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
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=80)),
                ('age', models.IntegerField(choices=[(1, '14-16'), (2, '17-19'), (3, '20-24'), (4, '25-30'), (5, '31-40'), (6, '+40')])),
                ('rating', models.FloatField(default=5.0)),
                ('number_of_ratings', models.PositiveSmallIntegerField(default=0)),
                ('location', models.GenericIPAddressField(blank=True, null=True)),
                ('owner', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
