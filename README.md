# Unab Residencia
# Datos iniciales
INSERT INTO auth_group values(0,'Default');
INSERT INTO auth_group values(1,'Admin');
INSERT INTO auth_group values(2,'Reciclador');
INSERT INTO auth_group values(3,'Recolector');

# Primer usuario administrador
Crear el primer usuario Admin Unab
    --> python manage.py createsuperuser (luego seguir las instrucciones)
    --> agregue el perfil con el siguiente query "INSERT INTO registration_profile VALUES(0,'Defaul',1,1);"


