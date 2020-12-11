# Generated by Django 3.1.4 on 2020-12-11 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=200)),
                ('model', models.CharField(max_length=200)),
                ('color', models.CharField(max_length=200)),
                ('price', models.FloatField()),
            ],
        ),
    ]
