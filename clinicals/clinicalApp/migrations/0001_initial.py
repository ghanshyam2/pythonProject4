# Generated by Django 4.0 on 2023-04-04 07:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lastName', models.CharField(max_length=150)),
                ('firstName', models.CharField(max_length=150)),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ClinicalData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('componentName', models.CharField(choices=[('hw', 'height/weight'), ('bp', 'Blood Pressure'), ('hr', 'Heart Rate')], max_length=166)),
                ('componentValues', models.CharField(max_length=166)),
                ('measureDateTime', models.DateTimeField(auto_now_add=True)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinicalApp.patient')),
            ],
        ),
    ]
