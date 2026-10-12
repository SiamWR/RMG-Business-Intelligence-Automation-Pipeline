from extract import (
    extract_factory,
    extract_product,
    extract_date,
    extract_production
)

from transform import (
    clean_factory,
    clean_product,
    clean_date,
    clean_production
)



factory = extract_factory()

product = extract_product()

date = extract_date()

production = extract_production()



factory_clean = clean_factory(factory)

product_clean = clean_product(product)

date_clean = clean_date(date)

production_clean = clean_production(production)



print(factory_clean.head())

print(product_clean.head())

print(date_clean.head())

print(production_clean.head())