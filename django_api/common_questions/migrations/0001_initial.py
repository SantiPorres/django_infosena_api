# Generated by Django 4.2.5 on 2023-09-20 13:37

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CommonQuestion',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('slug', models.SlugField(default='08464fc47322486c92eea26ae5a0b3ce', max_length=100, unique=True)),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], default='Active', max_length=8)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('question', models.CharField(default=uuid.UUID('309f8380-a5c1-410e-a9ea-291dddfd2213'), max_length=120, unique=True)),
                ('answer', models.TextField(default=uuid.UUID('5ea53d5f-5caa-4583-9a49-01348ad38fe4'), max_length=1000)),
            ],
            options={
                'verbose_name': 'common_question',
                'verbose_name_plural': 'common_questions',
            },
        ),
    ]
