# Generated by Django 3.0.7 on 2020-06-14 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='tags',
            field=models.ManyToManyField(to='books.Tag'),
        ),
        migrations.DeleteModel(
            name='tags',
        ),
    ]
