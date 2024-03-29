# Generated by Django 2.2 on 2019-09-27 08:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookManager', '0002_auto_20190927_0844'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='book_author',
        ),
        migrations.AddField(
            model_name='book',
            name='book_author',
            field=models.ManyToManyField(to='bookManager.Author'),
        ),
        migrations.AlterField(
            model_name='book',
            name='book_publish',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookManager.Publish'),
        ),
    ]
