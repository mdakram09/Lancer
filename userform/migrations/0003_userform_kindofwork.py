# Generated by Django 3.1.1 on 2022-04-15 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userform', '0002_auto_20220415_1035'),
    ]

    operations = [
        migrations.AddField(
            model_name='userform',
            name='kindofwork',
            field=models.CharField(max_length=100, null=True),
        ),
    ]