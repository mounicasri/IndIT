# Generated by Django 2.2.2 on 2019-06-13 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('dept', models.CharField(max_length=50)),
                ('photo', models.CharField(max_length=2083)),
            ],
        ),
    ]
