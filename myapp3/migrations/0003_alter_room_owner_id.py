# Generated by Django 4.1.4 on 2022-12-26 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp3', '0002_alter_room_owner_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='owner_id',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.PROTECT, to='myapp3.teacher'),
            preserve_default=False,
        ),
    ]
