# Generated by Django 3.0.3 on 2020-12-05 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authorization', '0005_auto_20201205_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercreate',
            name='username',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
