# Generated by Django 4.0 on 2021-12-16 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teamMember', '0005_teammember_adminorregular'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teammember',
            name='adminOrRegular',
            field=models.CharField(choices=[('0', 'Admin'), ('1', 'Regular')], max_length=11),
        ),
    ]