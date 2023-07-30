# Generated by Django 4.0.4 on 2022-05-21 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Citizen',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('firstName', models.CharField(max_length=200)),
                ('lastName', models.CharField(max_length=200)),
                ('dateOfBirth', models.DateTimeField()),
                ('cellular', models.IntegerField()),
                ('landLine', models.IntegerField()),
                ('address', models.CharField(max_length=200)),
                ('City', models.CharField(max_length=200)),
                ('zipCode', models.CharField(max_length=200)),
                ('hadCovid', models.CharField(max_length=200)),
                ('previousConditions', models.CharField(max_length=200)),
            ],
        ),
    ]
