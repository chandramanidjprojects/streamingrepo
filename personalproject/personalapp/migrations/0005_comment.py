# Generated by Django 4.1.3 on 2022-11-13 11:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('personalapp', '0004_alter_postlike_like_to'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.TextField(blank=True, null=True)),
                ('comment_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('comment_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='personalapp.post')),
            ],
        ),
    ]
