# Generated by Django 4.1.2 on 2023-05-05 20:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MetaData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('server_name', models.CharField(blank=True, max_length=255, null=True)),
                ('http_host', models.CharField(blank=True, max_length=255, null=True)),
                ('remote_addr', models.CharField(blank=True, max_length=255, null=True)),
                ('remote_host', models.CharField(blank=True, max_length=255, null=True)),
                ('remote_user', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name_plural': 'Meta Data',
            },
        ),
    ]