# Generated by Django 4.1 on 2022-08-28 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bsyrr', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
            ],
        ),
    ]
