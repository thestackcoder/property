# Generated by Django 3.1.5 on 2021-01-16 22:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SmallText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media')),
                ('title', models.CharField(max_length=255)),
                ('text', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='smalltext', to='project.project')),
            ],
        ),
        migrations.CreateModel(
            name='LargeTextSubsection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('text', models.TextField()),
                ('largetext', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='largetext_subsection', to='project.largetext')),
            ],
        ),
    ]
