# Generated by Django 4.0 on 2021-12-16 07:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teamMember', '0003_alter_teammember_email_alter_teammember_phonenumber'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teammember',
            name='adminOrRegular',
        ),
    ]
