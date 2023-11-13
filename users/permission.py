# from django.contrib.auth.models import Permission, Group
# from users.models import Profile 

# # Define and assign permissions here
# author_group = Group.objects.get_or_create(name='AuthorUser')[0]
# app_group = Group.objects.get_or_create(name='AppUser')[0]

# # Define permissions for Type1User
# author_permissions = Permission.objects.filter(
#     codename__in=['permission1_type1', 'permission2_type1']
# )
# type1_group.permissions.add(*type1_permissions)

# # Define permissions for Type2User
# app_permissions = Permission.objects.filter(
#     codename__in=['permission1_type2', 'permission2_type2']
# )
# type2_group.permissions.add(*type2_permissions)
