# Generated by Django 2.0.7 on 2021-12-13 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teamMember', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teammember',
            name='adminOrRegular',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='teammember',
            name='email',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='teammember',
            name='firstName',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='teammember',
            name='lastName',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='teammember',
            name='phoneNumber',
            field=models.CharField(max_length=255),
        ),
    ]
