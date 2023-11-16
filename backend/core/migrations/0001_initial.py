# Generated by Django 4.2.3 on 2023-11-16 20:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Date and time where this record was created.')),
                ('last_modified_at', models.DateTimeField(auto_now=True, help_text='Date and time of this record last edition.')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, help_text='ID generated by system', primary_key=True, serialize=False)),
                ('name', models.CharField(db_index=True, help_text='Name of the game. Unique. Ex: Age of Empires II.', max_length=128, unique=True)),
            ],
            options={
                'verbose_name': 'game',
                'verbose_name_plural': 'games',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Playable',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Date and time where this record was created.')),
                ('last_modified_at', models.DateTimeField(auto_now=True, help_text='Date and time of this record last edition.')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, help_text='ID generated by system', primary_key=True, serialize=False)),
                ('name', models.CharField(db_index=True, help_text='Name of the game. Unique. Ex: Age of Empires II.', max_length=128, unique=True)),
                ('game', models.ForeignKey(help_text='The game to which this playable belongs', on_delete=django.db.models.deletion.CASCADE, related_name='playables', to='core.game')),
            ],
            options={
                'verbose_name': 'playable',
                'verbose_name_plural': 'playables',
                'ordering': ['game', 'name'],
            },
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, help_text='ID generated by system', primary_key=True, serialize=False)),
                ('datetime_start', models.DateTimeField(blank=True, help_text='Date and time for the match to start', null=True)),
                ('datetime_end', models.DateTimeField(blank=True, help_text='Date and time when the match ended', null=True)),
                ('game', models.ForeignKey(help_text='The game played at this match', on_delete=django.db.models.deletion.PROTECT, related_name='matches', to='core.game')),
            ],
            options={
                'verbose_name': 'match',
                'verbose_name_plural': 'matches',
                'ordering': ['game', '-datetime_start'],
            },
        ),
        migrations.CreateModel(
            name='Contender',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, help_text='ID generated by system', primary_key=True, serialize=False)),
                ('is_winner', models.BooleanField(default=False, help_text='This contender won the match')),
                ('match', models.ForeignKey(help_text='Match played by the contender', on_delete=django.db.models.deletion.CASCADE, related_name='contenders', to='core.match')),
                ('playable', models.ForeignKey(blank=True, help_text='Playable used by the contender at the match', null=True, on_delete=django.db.models.deletion.PROTECT, to='core.playable')),
                ('user', models.ForeignKey(blank=True, help_text='User playing this match. If null, it means that user was deleted', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='matches', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'contender',
                'verbose_name_plural': 'contenders',
                'ordering': ['match'],
            },
        ),
    ]
