# Generated by Django 3.1.5 on 2021-01-20 22:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_carouselitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='FloorPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media')),
            ],
        ),
        migrations.CreateModel(
            name='FloorPlanSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media')),
                ('title', models.CharField(max_length=255)),
                ('boundaries', models.CharField(max_length=50)),
                ('floorplan', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='project.floorplan')),
            ],
        ),
        migrations.CreateModel(
            name='CarouselVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to='media/files')),
                ('carouselItem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.carouselitem')),
            ],
        ),
        migrations.CreateModel(
            name='CarouselPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='media')),
                ('carouselItem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.carouselitem')),
            ],
        ),
    ]