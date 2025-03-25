from sqlalchemy.orm import Session
from app.enums.roles_enum import Roles
from app.models.role_model import Role
from app.schemas.role_schema import RoleCreate
from app.services.role_service import create_role

ROLES = [
    {
        'name': Roles.ROOT.value, 
        'description':'System Administrator and all permissions'
    },
    {
        'name': Roles.ADMIN.value, 
        'description':'System Administrator'
    },
    {
        'name': Roles.EDITOR.value, 
        'description':'User with editing permissions'
    },
    {
        'name': Roles.USER.value, 
        'description':'Basic User'
    },
    {
        'name': Roles.GUEST.value, 
        'description':'Guest User'
    }
]

def seed_roles(session: Session):
    from app.database.seeds.role_seed import ROLES
    existing_roles = session.query(Role).count()
    if existing_roles == 0:
        for role_data in ROLES:
            role_create = RoleCreate(**role_data)
            create_role(db=session, role_data=role_create)
        print(f'{len(ROLES)} ROLES inserted correctly.')
    else:
        print('The ROLES data already exists, it will not be inserted again.')