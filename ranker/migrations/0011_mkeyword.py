# Generated by Django 3.2.8 on 2021-11-24 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ranker', '0010_alter_conferencedata_abbrv'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mkeyword',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField(default='NULL', help_text='keyword for search', max_length=100)),
                ('frequency', models.IntegerField(help_text='Pages already seen')),
            ],
        ),
    ]