# Generated by Django 3.0 on 2021-08-26 05:21

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
                ('ename', models.CharField(max_length=120)),
                ('empid', models.CharField(max_length=10)),
                ('ememail', models.EmailField(max_length=120)),
            ],
        ),
    ]