# Generated by Django 2.1.5 on 2019-03-21 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0012_auto_20190321_2103'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nc1products',
            name='filter',
        ),
        migrations.RemoveField(
            model_name='nc2products',
            name='filter',
        ),
        migrations.RemoveField(
            model_name='nc3products',
            name='filter',
        ),
        migrations.DeleteModel(
            name='NC1Filters',
        ),
        migrations.DeleteModel(
            name='NC2Filters',
        ),
        migrations.DeleteModel(
            name='NC3Filters',
        ),
    ]
