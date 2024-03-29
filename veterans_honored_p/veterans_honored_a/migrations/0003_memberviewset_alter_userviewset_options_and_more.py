# Generated by Django 4.1.7 on 2023-05-21 18:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('veterans_honored_a', '0002_user_member'),
    ]

    operations = [
        migrations.CreateModel(
            name='MemberViewSet',
            fields=[
                ('member_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='veterans_honored_a.member')),
            ],
            bases=('veterans_honored_a.member',),
        ),
        migrations.AlterModelOptions(
            name='userviewset',
            options={},
        ),
        migrations.AlterModelManagers(
            name='userviewset',
            managers=[
            ],
        ),
        migrations.AlterField(
            model_name='userviewset',
            name='user_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='veterans_honored_a.user'),
        ),
    ]
