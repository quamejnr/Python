from dataclasses import dataclass

@dataclass
class Category:
    main_category: str
    sub_category: str 
    
@dataclass
class Product:
    name: str
    product_id: str
    product_description: str
    category: Category  
    directions_for_use: str
    
@dataclass
class ProductAlias:
    name: str
    display_name: str
    product: Product