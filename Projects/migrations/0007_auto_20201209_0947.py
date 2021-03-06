# Generated by Django 3.1.3 on 2020-12-09 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Projects', '0006_auto_20201208_1758'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_files',
            field=models.FileField(blank=True, null=True, upload_to='static/project/files'),
        ),
        migrations.AlterField(
            model_name='project',
            name='git_link',
            field=models.URLField(blank=True, null=True, verbose_name='External Project Files Link'),
        ),
    ]
