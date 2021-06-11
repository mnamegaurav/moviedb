# Generated by Django 3.2.4 on 2021-06-11 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('added_on', 'updated_on')},
        ),
        migrations.AlterModelOptions(
            name='movie',
            options={'ordering': ('added_on', 'updated_on')},
        ),
        migrations.AddField(
            model_name='movie',
            name='title',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]