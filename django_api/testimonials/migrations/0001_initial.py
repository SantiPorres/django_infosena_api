# Generated by Django 4.2.5 on 2023-09-20 12:58

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Testimony',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('slug', models.SlugField(default='9d910d7ace0947d6b4c45f4bbac06114', max_length=100, unique=True)),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], default='Active', max_length=8)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('testimony', models.CharField(default=uuid.UUID('602f3635-5d4c-48d6-a6bc-3b9e961ae23f'), max_length=500)),
                ('witness_name', models.CharField(blank=True, max_length=120, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='testimonials')),
            ],
            options={
                'verbose_name': 'testimony',
                'verbose_name_plural': 'testimonies',
            },
        ),
    ]