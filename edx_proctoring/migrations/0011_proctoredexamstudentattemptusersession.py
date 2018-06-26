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
            name='ProctoredExamStudentAttemptUserSession',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('session_id', models.CharField(max_length=255, db_index=True)),
                ('user_agent', models.TextField()),
                ('ip_address', models.CharField(max_length=255)),
                ('hidden', models.BooleanField(default=False)),
                ('attempt', models.ForeignKey(to='edx_proctoring.ProctoredExamStudentAttempt')),
            ],
            options={
                'db_table': 'proctoring_proctoredexamstudentattempt_usersession',
                'verbose_name': 'proctored exam attempt user session',
            },
        ),
        migrations.AlterUniqueTogether(
            name='proctoredexamstudentattemptusersession',
            unique_together=set([('attempt', 'session_id')]),
        ),
    ]
