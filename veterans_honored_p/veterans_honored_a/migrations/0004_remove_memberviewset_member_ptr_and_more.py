# Generated by Django 4.1.7 on 2023-05-21 18:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('veterans_honored_a', '0003_memberviewset_alter_userviewset_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='memberviewset',
            name='member_ptr',
        ),
        migrations.RemoveField(
            model_name='userviewset',
            name='user_ptr',
        ),
        migrations.DeleteModel(
            name='GroupViewSet',
        ),
        migrations.DeleteModel(
            name='MemberViewSet',
        ),
        migrations.DeleteModel(
            name='UserViewSet',
        ),
    ]
