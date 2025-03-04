from app.enums.roles_enum import Roles

ROLES = [
    {'name': Roles.ROOT.value, 'description':'Administrador del sistema y todos los permisos'},
    {'name': Roles.ADMIN.value, 'description':'Administrador del sistema'},
    {'name': Roles.EDITOR.value, 'description':'Usuario con permisos de edición'},
    {'name': Roles.USER.value, 'description':'Usuario básico'},
    {'name': Roles.GUEST.value, 'description':'Usuario invitado'}
]