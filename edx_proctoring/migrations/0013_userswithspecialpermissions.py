# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


def migrate_users(apps, schema_editor):
    User = apps.get_model("auth", "User")
    UsersWithSpecialPermissions = apps.get_model("edx_proctoring", "UsersWithSpecialPermissions")

    if hasattr(settings, 'USERS_WITH_SPECIAL_PERMS_IDS') and settings.USERS_WITH_SPECIAL_PERMS_IDS:
        users = User.objects.filter(id__in=settings.USERS_WITH_SPECIAL_PERMS_IDS)
        for u in users:
            UsersWithSpecialPermissions(user=u).save()


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('edx_proctoring', '0012_proctoredexamstudentattemptstopreason'),
    ]

    operations = [
        migrations.CreateModel(
            name='UsersWithSpecialPermissions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.OneToOneField(related_name='special_permissions', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'proctoring_users_with_special_permissions',
                'verbose_name': 'users with special permissions',
            },
        ),
        migrations.RunPython(
            migrate_users,
        ),
    ]
