from sqlalchemy.orm import Session
from app.enums.image_type_enum import ImageType
from app.models.product_model import Product
from app.schemas.product_schema import ProductCreate
from app.services.product_service import create_product
from app.schemas.image_schema import ImageCreate
from app.services.image_service import create_image

PRODUCTS = [
    {
        'name': 'Baby Yoda Blueball', 
        'description': 'Figura coleccionable de Baby Yoda (Grogu) - The Mandalorian Saga, edición limitada.', 
        'price': 1799.99, 
        'stock': 8, 
        'discount': 5.00, 
        'sku': 'STW001001', 
        'dues': 3, 
        'special': 0, 
        'licence_id': 2, 
        'category_id': 1,
        'images': [
            {
                'path': 'images/star-wars/funkos/baby-yoda-blueball_front.webp',
                'image_type': ImageType.FRONT.lower(),
                'is_primary': True
            },
            {
                'path': 'images/star-wars/funkos/baby-yoda-blueball_back.webp',
                'image_type': ImageType.BACK.lower(),
                'is_primary': False
            }
        ]
    },
    {
        'name': 'Luke Skylwalker & Grogu', 
        'description': 'Figura coleccionable de Luke Skylwalker & Grogu - The Mandalorian Saga.', 
        'price': 2399.99, 
        'stock': 8, 
        'discount': 15.00, 
        'sku': 'STW001003', 
        'dues': 3, 
        'special': 0, 
        'licence_id': 2, 
        'category_id': 1,
        'images': [
            {
                'path': 'images/star-wars/funkos/luke-skylwalker-&-grogu_front.webp',
                'image_type': ImageType.FRONT.lower(),
                'is_primary': True
            },
            {
                'path': 'images/star-wars/funkos/luke-skylwalker-&-grogu_back.webp',
                'image_type': ImageType.BACK.lower(),
                'is_primary': False
            }
        ]
    },
    {
        'name': 'Stormtrooper Lightsaber', 
        'description': 'Figura coleccionable de Stormtrooper Lightsaber - Star Wars Saga.', 
        'price': 1799.99, 
        'stock': 8, 
        'discount': 20.00, 
        'sku': 'STW001004', 
        'dues': 3, 
        'special': 0, 
        'licence_id': 2, 
        'category_id': 1,
        'images': [
            {
                'path': 'images/star-wars/funkos/stormtrooper-lightsaber_front.webp',
                'image_type': ImageType.FRONT.lower(),
                'is_primary': True
            },
            {
                'path': 'images/star-wars/funkos/stormtrooper-lightsaber_back.webp',
                'image_type': ImageType.BACK.lower(),
                'is_primary': False
            }
        ]
    },
    {
        'name': 'Charmander Smiley', 
        'description': 'Figura coleccionable de Charmander - Pokemon Saga.', 
        'price': 1799.99, 
        'stock': 8, 
        'discount': 10.00, 
        'sku': 'PKM001001', 
        'dues': 3, 
        'special': 0, 
        'licence_id': 1, 
        'category_id': 1,
        'images': [
            {
                'path': 'images/pokemon/funkos/charmander-smiley_front.webp',
                'image_type': ImageType.FRONT.lower(),
                'is_primary': True
            },
            {
                'path': 'images/pokemon/funkos/charmander-smiley_back.webp',
                'image_type': ImageType.BACK.lower(),
                'is_primary': False
            }
        ]
    },
    {
        'name': 'Dragonite Hi!', 
        'description': 'Figura coleccionable de Dragonite - Pokemon Saga.', 
        'price': 1799.99, 
        'stock': 8, 
        'discount': 10.00, 
        'sku': 'PKM001002', 
        'dues': 3, 
        'special': 0, 
        'licence_id': 1, 
        'category_id': 1,
        'images': [
            {
                'path': 'images/pokemon/funkos/dragonite-hi!_front.webp',
                'image_type': ImageType.FRONT.lower(),
                'is_primary': True
            },
            {
                'path': 'images/pokemon/funkos/dragonite-hi!_back.webp',
                'image_type': ImageType.BACK.lower(),
                'is_primary': False
            }
        ]
    },
    {
        'name': 'Pidgeotto Flying', 
        'description': 'Figura coleccionable de Pidgeotto - Pokemon Saga.', 
        'price': 1799.99, 
        'stock': 8, 
        'discount': 30.00, 
        'sku': 'PKM00103', 
        'dues': 3, 
        'special': 1, 
        'licence_id': 1, 
        'category_id': 1,
        'images': [
            {
                'path': 'images/pokemon/funkos/pidgeotto-flying_front.webp',
                'image_type': ImageType.FRONT.lower(),
                'is_primary': True
            },
            {
                'path': 'images/pokemon/funkos/pidgeotto-flying_back.webp',
                'image_type': ImageType.BACK.lower(),
                'is_primary': False
            }
        ]
    },
    {
        'name': 'Pikachu Smiley', 
        'description': 'Figura coleccionable de Pikachu - Pokemon Saga.', 
        'price': 1799.99, 
        'stock': 8, 
        'discount': 10.00, 
        'sku': 'PKM001004', 
        'dues': 3, 
        'special': 0, 
        'licence_id': 1, 
        'category_id': 1,
        'images': [
            {
                'path': 'images/pokemon/funkos/pikachu-smiley_front.webp',
                'image_type': ImageType.FRONT.lower(),
                'is_primary': True
            },
            {
                'path': 'images/pokemon/funkos/pikachu-smiley_back.webp',
                'image_type': ImageType.BACK.lower(),
                'is_primary': False
            }
        ]
    },
    {
        'name': 'Vulpix Fancy', 
        'description': 'Figura coleccionable de Vulpix - Pokemon Saga.', 
        'price': 99.99, 
        'stock': 8, 
        'discount': 10.00, 
        'sku': 'PKM001005', 
        'dues': 3, 
        'special': 0, 
        'licence_id': 1, 
        'category_id': 1,
        'images': [
            {
                'path': 'images/pokemon/funkos/vulpix-fancy_front.webp',
                'image_type': ImageType.FRONT.lower(),
                'is_primary': True
            },
            {
                'path': 'images/pokemon/funkos/vulpix-fancy_back.webp',
                'image_type': ImageType.BACK.lower(),
                'is_primary': False
            }
        ]
    },
    {
        'name': 'Harry Potter & Hegwid', 
        'description': 'Figura coleccionable de Harry Potter & Hegwid - Harry Potter Saga.', 
        'price': 1799.99, 
        'stock': 11, 
        'discount': 10.00, 
        'sku': 'HPT001001', 
        'dues': 9, 
        'special': 0, 
        'licence_id': 3, 
        'category_id': 1,
        'images': [
            {
                'path': 'images/harry-potter/funkos/harry-Potter-&-hegwid_front.webp',
                'image_type': ImageType.FRONT.lower(),
                'is_primary': True
            },
            {
                'path': 'images/harry-potter/funkos/harry-Potter-&-hegwid_back.webp',
                'image_type': ImageType.BACK.lower(),
                'is_primary': False
            }
        ]
    },
    {
        'name': 'Kakashi Hatake Shippuden', 
        'description': 'Kakashi Hatake Shippuden', 
        'price': 1999.99, 
        'stock': 20, 
        'discount': 10.00, 
        'sku': 'NRT001001', 
        'dues': 9, 
        'special': 0, 
        'licence_id': 4, 
        'category_id': 1,
        'images': [
            {
                'path': 'images/naruto/funkos/kakashi-hatake-shippuden_front.webp',
                'image_type': ImageType.FRONT.lower(),
                'is_primary': True
            },
            {
                'path': 'images/naruto/funkos/kakashi-hatake-shippuden_back.webp',
                'image_type': ImageType.BACK.lower(),
                'is_primary': False
            }
        ]
    },
    {
        'name': 'Harry Potter', 
        'description': 'Remera coleccionable de Harry Potter.', 
        'price': 100.00, 
        'stock': 999, 
        'discount': 10.00, 
        'sku': 'HPT003001', 
        'dues': 6, 
        'special': 1, 
        'licence_id': 3, 
        'category_id': 2,
        'images': [
            {
                'path': 'images/harry-potter/t-shirts/harry-potter_front.webp',
                'image_type': ImageType.FRONT.lower(),
                'is_primary': True
            },
            {
                'path': 'images/harry-potter/t-shirts/harry-potter_back.webp',
                'image_type': ImageType.BACK.lower(),
                'is_primary': False
            }
        ]
    },
    {
        'name': 'Goku with Kamehameha', 
        'description': 'LLavero coleccionable de Goku.', 
        'price': 100.00, 
        'stock': 999, 
        'discount': 10.00, 
        'sku': 'DBZ003001', 
        'dues': 6, 
        'special': 1, 
        'licence_id': 5, 
        'category_id': 3,
        'images': [
            {
                'path': 'images/dragon-ball/keychains/goku-with-kamehameha_front.webp',
                'image_type': ImageType.FRONT.lower(),
                'is_primary': True
            },
            {
                'path': 'images/dragon-ball/keychains/goku-with-kamehameha_back.webp',
                'image_type': ImageType.BACK.lower(),
                'is_primary': False
            }
        ]
    }
]

def seed_products(session: Session):    
    existing_products = session.query(Product).count()
    if existing_products == 0:
        for product_data in PRODUCTS:
            product_create = ProductCreate(**product_data)
            db_product = create_product(db=session, product_data=product_create)
            if db_product:
                if 'images' in product_data and isinstance(product_data['images'], list):
                    for image_data in product_data['images']:                        
                        image_create = ImageCreate(
                            path=image_data['path'],
                            entity_type='product',
                            entity_id=db_product.id,
                            image_type=image_data['image_type'],
                            is_primary=image_data['is_primary']
                        )                        
                        create_image(db=session, image=image_create)
        print(f'{len(PRODUCTS)} PRODUCTS inserted correctly.')
    else:
        print('The PRODUCTS data already exists, it will not be inserted again.')