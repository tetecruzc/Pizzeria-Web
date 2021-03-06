# Generated by Django 3.1.6 on 2021-02-03 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Drink',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('price', models.DecimalField(decimal_places=2, max_digits=20)),
            ],
        ),
        migrations.AddField(
            model_name='pizza',
            name='drinks',
            field=models.ManyToManyField(blank=True, to='pizzas.Drink'),
        ),
    ]
