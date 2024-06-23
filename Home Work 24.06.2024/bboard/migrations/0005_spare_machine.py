# Generated by Django 5.0.6 on 2024-06-10 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0004_alter_bb_content_alter_bb_kind_alter_bb_price_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Spare',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('spares', models.ManyToManyField(to='bboard.spare')),
            ],
        ),
    ]