# Generated by Django 4.0.4 on 2022-04-19 21:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HospitalAPI', '0012_alter_patientscardiac_patientcpf'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patients',
            name='id',
        ),
        migrations.AlterField(
            model_name='patients',
            name='cpf',
            field=models.CharField(max_length=14, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='patientspulmonary',
            name='patientCPF',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, related_name='pulmonary', to='HospitalAPI.patients'),
            preserve_default=False,
        ),
    ]
