# Generated by Django 4.1.1 on 2022-10-04 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ratingbeer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beer',
            name='country',
            field=models.CharField(max_length=255, null=True, verbose_name='Страна'),
        ),
        migrations.AlterField(
            model_name='beer',
            name='image',
            field=models.ImageField(blank=True, upload_to='media/%Y/%m/%d', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='beer',
            name='price',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Цена'),
        ),
        migrations.AddConstraint(
            model_name='rating',
            constraint=models.CheckConstraint(check=models.Q(('rate__range', (0, 10))), name='valid_rate'),
        ),
        migrations.DeleteModel(
            name='Country',
        ),
    ]
