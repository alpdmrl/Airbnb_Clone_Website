# Generated by Django 3.2.16 on 2023-04-25 10:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myApp', '0003_post_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profil',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('isim', models.CharField(max_length=50)),
                ('soyisim', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('profilresim', models.FileField(blank=True, default='profilpic/default.jpg', upload_to='profilpic/')),
                ('meslek', models.CharField(max_length=50)),
                ('slug', models.SlugField(blank=True, editable=False, null=True, unique=True)),
                ('kullanici', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]