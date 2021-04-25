# Generated by Django 3.1.7 on 2021-04-09 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaModel',
            fields=[
                ('categoriaId', models.AutoField(db_column='categoria_id', primary_key=True, serialize=False)),
                ('categoriaNombre', models.CharField(db_column='categoria_nombre', max_length=40, verbose_name='Nombre de categoria')),
            ],
            options={
                'verbose_name': 'Categoria',
                'db_table': 't_categoria',
            },
        ),
        migrations.CreateModel(
            name='UsuarioModel',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('usuarioId', models.AutoField(db_column='personal_id', primary_key=True, serialize=False, unique=True)),
                ('usuarioCorreo', models.EmailField(db_column='usuario_correo', max_length=30, unique=True, verbose_name='Correo del personal')),
                ('usuarioTipo', models.IntegerField(choices=[(1, 'ADMINISTRADOR'), (2, 'USUARIO')], db_column='usuario_tipo', verbose_name='Tipo del personal')),
                ('usuarioNombre', models.CharField(db_column='usuario_nombre', max_length=45, verbose_name='Nombre del personal')),
                ('usuarioApellido', models.CharField(db_column='usuario_apellido', max_length=45, verbose_name='Apellido del personal')),
                ('password', models.TextField(db_column='usuario_contrasena', verbose_name='Contraseña del personal')),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'usaurio',
                'verbose_name_plural': 'usuarios',
                'db_table': 't_usuario',
            },
        ),
    ]
