# Generated by Django 2.1.7 on 2019-03-20 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20190315_1232'),
    ]

    operations = [
        migrations.AddField(
            model_name='paidordersnc1',
            name='order_comments',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='paidordersnc2',
            name='order_comments',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='paidordersnc3',
            name='order_comments',
            field=models.TextField(blank=True, null=True),
        ),
    ]
