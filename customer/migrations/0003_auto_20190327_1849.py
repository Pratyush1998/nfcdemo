# Generated by Django 2.0.7 on 2019-03-27 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_auto_20190327_1810'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerinfo',
            name='cardNumber',
            field=models.CharField(default=' ', max_length=16),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customerinfo',
            name='customerId',
            field=models.CharField(default=' ', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customerinfo',
            name='email',
            field=models.CharField(default=' ', max_length=50),
            preserve_default=False,
        ),
    ]
