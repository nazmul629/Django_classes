# Generated by Django 2.0.7 on 2018-08-03 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_blog', '0003_auto_20180803_0449'),
    ]

    operations = [
        migrations.CreateModel(
            name='Catagory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
