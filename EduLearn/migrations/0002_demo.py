# Generated by Django 2.0.2 on 2019-01-14 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edulearn', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Demo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=200)),
                ('lname', models.CharField(max_length=200)),
            ],
        ),
    ]
