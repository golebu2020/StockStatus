# Generated by Django 3.2.4 on 2024-03-25 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(choices=[('red', 'Red'), ('grey', 'Grey'), ('black', 'Black'), ('white', 'White'), ('purple', 'Purple')], default='red', max_length=100)),
                ('availability', models.CharField(choices=[('available', 'Available'), ('out of stock', 'Out of Stock'), ('running low', 'Running Low')], default='available', max_length=100)),
                ('inventory', models.IntegerField()),
            ],
        ),
    ]
