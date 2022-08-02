# Generated by Django 4.0.3 on 2022-06-28 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, null=True, verbose_name='Full Name')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('bio', models.TextField(verbose_name='User Bio')),
            ],
        ),
    ]