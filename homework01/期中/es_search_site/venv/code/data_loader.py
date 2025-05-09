from es_client import es

products = [
    {"name": "iPhone 15", "description": "Apple smartphone"},
    {"name": "MacBook Pro", "description": "Powerful laptop from Apple"},
    {"name": "Galaxy S24", "description": "Samsung smartphone"},
]

for i, product in enumerate(products):
    es.index(index="products", id=i, document=product)

es.indices.refresh(index="products")
print("Data loaded.")
