# Generated by Django 3.2.11 on 2022-01-27 12:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20220127_1510'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articles',
            options={'verbose_name': 'Новость', 'verbose_name_plural': 'Новости'},
        ),
        migrations.RenameField(
            model_name='articles',
            old_name='Anons',
            new_name='anons',
        ),
        migrations.RenameField(
            model_name='articles',
            old_name='Date',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='articles',
            old_name='Full_info',
            new_name='full_info',
        ),
        migrations.RenameField(
            model_name='articles',
            old_name='Title',
            new_name='title',
        ),
    ]
