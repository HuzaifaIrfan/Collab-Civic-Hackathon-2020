# Generated by Django 3.1.3 on 2020-12-07 12:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Projects', '0001_initial'),
        ('socialaccount', '0001_initial'),
        ('Universities', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='social_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='socialaccount.socialaccount'),
        ),
        migrations.AddField(
            model_name='project',
            name='university',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Universities.universities'),
        ),
    ]