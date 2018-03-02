# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('edx_proctoring', '0010_proctoredexamstudentattemptcustom'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProctoredExamRoom',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('testing_center', models.CharField(max_length=1024)),
                ('status', models.CharField(default=b'in_progress', max_length=11, choices=[(b'in_progress', 'In progress'), (b'archived', 'Archived')])),
                ('exam', models.ForeignKey(related_name='rooms', to='edx_proctoring.ProctoredExam')),
            ],
            options={
                'db_table': 'proctoring_proctoredexamroom',
                'verbose_name': 'proctored exam room',
            },
        ),
    ]
