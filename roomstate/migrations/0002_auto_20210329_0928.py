# Generated by Django 3.1.7 on 2021-03-29 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roomstate', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roomstate',
            name='room_state',
            field=models.CharField(choices=[('DND', 'Bitte nicht stören!'), ('OPN', 'Wir haben geöffnet!'), ('CLS', 'Wir haben geschlossen!'), ('BRB', 'Wir haben gleich wieder geöffnet!')], default='OPN', max_length=3),
        ),
    ]