from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Group
from .models import CustomUser

staff = Group.objects.get(name="staff")
admin = Group.objects.get(name="superuser")
content_type = ContentType.objects.get_for_model(CustomUser)

permission_add_admin = Permission.objects.create(
    codename='can_add_admin',
    name='Can Add Admin',
    content_type=content_type,
)

permission_change_page = Permission.objects.create(
    codename='can_change_big_pages',
    name='Can Change Big Pages',
    content_type=content_type,
)

permission_access = Permission.objects.create(
    codename='hav_access_to_admin ',
    name='Hav Access to Admin',
    content_type=content_type,
)

staff.permissions.add(permission_access)
admin.permissions.add(permission_add_admin, permission_change_page, permission_access)
