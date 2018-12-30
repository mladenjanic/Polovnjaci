# Generated by Django 2.1.4 on 2018-12-27 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0005_auto_20181227_1330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fleet',
            name='broj_vrata',
            field=models.CharField(choices=[('2/3', '2/3'), ('4/5', '4/5')], max_length=200),
        ),
        migrations.AlterField(
            model_name='fleet',
            name='gorivo',
            field=models.CharField(choices=[('Dizel', 'Dizel'), ('Benzin', 'Benzin'), ('Benzin + TNG', 'Benzin + TNG'), ('Metan CNG', 'Metan CNG'), ('Hibrid', 'Hibrid')], max_length=200),
        ),
    ]