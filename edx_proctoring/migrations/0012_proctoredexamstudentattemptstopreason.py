# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edx_proctoring', '0011_proctoredexamstudentattemptusersession'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProctoredExamStudentAttemptStopReason',
            fields=[
                ('attempt', models.OneToOneField(related_name='stop_reason', primary_key=True, serialize=False, to='edx_proctoring.ProctoredExamStudentAttempt')),
                ('reason', models.TextField()),
                ('proctor', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'proctoring_proctoredexamstudentattempt_stopreason',
                'verbose_name': 'proctored exam attempt stop reason',
            },
        ),
    ]