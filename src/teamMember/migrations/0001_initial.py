# Generated by Django 2.0.7 on 2021-12-13 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='teamMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.TextField()),
                ('lastName', models.TextField()),
                ('email', models.TextField()),
                ('phoneNumber', models.TextField()),
                ('adminOrRegular', models.TextField()),
            ],
        ),
    ]
