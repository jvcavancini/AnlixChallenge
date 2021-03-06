# Generated by Django 4.0.4 on 2022-04-18 22:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HospitalAPI', '0005_patients_id_alter_patients_cpf_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientscardiac',
            name='patientCPF',
            field=models.ForeignKey(db_column='cpf', on_delete=django.db.models.deletion.CASCADE, to='HospitalAPI.patients', to_field='cpf'),
        ),
        migrations.AlterField(
            model_name='patientspulmonary',
            name='patientCPF',
            field=models.ForeignKey(db_column='cpf', on_delete=django.db.models.deletion.CASCADE, to='HospitalAPI.patients', to_field='cpf'),
        ),
    ]
