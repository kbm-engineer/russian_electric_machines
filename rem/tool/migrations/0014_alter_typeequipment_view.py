# Generated by Django 4.2.3 on 2023-08-07 17:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tool', '0013_basemonitoringobject_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='typeequipment',
            name='view',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tool.viewequipment'),
        ),
    ]
