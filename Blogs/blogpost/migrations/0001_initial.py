# Generated by Django 4.0 on 2023-04-15 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, unique=True)),
                ('slug', models.SlugField(max_length=150, unique=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('content', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[(0, 'Draft'), (1, 'Published')], default=0, max_length=60)),
                ('auther', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts', to='auth.user')),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]
