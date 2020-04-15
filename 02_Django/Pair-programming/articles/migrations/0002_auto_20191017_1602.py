# Generated by Django 2.2.6 on 2019-10-17 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
            ],
            options={
                'ordering': ('-pk',),
            },
        ),
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ('-pk',)},
        ),
    ]