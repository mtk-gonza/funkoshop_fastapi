from sqlalchemy.orm import Session
from app.enums.image_type_enum import ImageType
from app.models.licence_model import Licence
from app.schemas.licence_schema import LicenceCreate
from app.services.licence_service import create_licence
from app.schemas.image_schema import ImageCreate
from app.services.image_service import create_image

LICENCES = [
    {
        'name':'Pokemon', 
        'description':'Atrapa todos los que puedas y disfruta de una colección llena de amigos.',
        'images': [
            {
                'path': 'images/pokemon/licence/pokemon_logo.webp',
                'image_type': ImageType.LOGO.lower(),
                'is_primary': True
            }
        ] 
    },
    {
        'name':'Star Wars', 
        'description':'Disfruta de una saga que sigue agregando personajes a su colección.', 
        'images': [
            {
                'path': 'images/star-wars/licence/star-wars_logo.webp',
                'image_type': ImageType.LOGO.lower(),
                'is_primary': True
            }
        ] 
    },
    {        
        'name':'Harry Potter', 
        'description':'Revive los recuerdos de una saga llena de magia y encanto.', 
        'images': [
            {
                'path': 'images/harry-potter/licence/harry-potter_logo.webp',
                'image_type': ImageType.LOGO.lower(),
                'is_primary': True
            }
        ] 
    },
    {
        'name':'Naruto', 
        'description':'Disfruta de la historia de un ninja adolescente', 
        'images': [
            {
                'path': 'images/Naruto/licence/naruto_logo.webp',
                'image_type': ImageType.LOGO.lower(),
                'is_primary': True
            }
        ] 
    },
    {
        'name':'Dragon Ball', 
        'description':'Disfruta de la historia de un guerrero saiyajin', 
        'images': [
            {
                'path': 'images/dragon-ball/licence/dragon-ball_logo.webp',
                'image_type': ImageType.LOGO.lower(),
                'is_primary': True
            }
        ] 
    }
]

def seed_licences(session: Session):    
    existing_licences = session.query(Licence).count()
    if existing_licences == 0:
        for licence_data in LICENCES:
            licence_create = LicenceCreate(**licence_data)
            db_licence = create_licence(db=session, licence=licence_create)
            if db_licence:                   
                if 'images' in licence_data and isinstance(licence_data['images'], list):
                    for image_data in licence_data['images']:                        
                        image_create = ImageCreate(
                            path=image_data['path'],
                            entity_type='licence',
                            entity_id=db_licence.id,
                            image_type=image_data['image_type'],
                            is_primary=image_data['is_primary']
                        )                        
                        create_image(db=session, image=image_create)
        print(f'{len(LICENCES)} LICENCES inserted correctly.')
    else:
        print('The LICENCES data already exists, it will not be inserted again.')