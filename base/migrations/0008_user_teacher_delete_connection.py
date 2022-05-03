# Generated by Django 4.0.4 on 2022-05-03 13:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_connection'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='student', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Connection',
        ),
    ]
