# =====================================================
# RMG BI AUTOMATION ETL PIPELINE
# =====================================================


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
    validate_production,
    clean_production
)


from load import (
    load_factory,
    load_product,
    load_date,
    load_production,
    load_errors
)



# =====================================================
# MAIN PIPELINE FUNCTION
# =====================================================


def run_pipeline():

    print("=" * 60)
    print("RMG BI AUTOMATION PIPELINE STARTED")
    print("=" * 60)



    # =================================================
    # 1. EXTRACT PHASE
    # =================================================

    print("\n[1] EXTRACT PHASE")


    factory_df = extract_factory()


    product_df = extract_product()


    date_df = extract_date()


    production_df = extract_production()



    # =================================================
    # 2. VALIDATION PHASE
    # =================================================

    print("\n[2] DATA VALIDATION PHASE")


    production_errors = validate_production(
        production_df
    )


    load_errors(
        production_errors
    )



    # =================================================
    # 3. TRANSFORMATION PHASE
    # =================================================

    print("\n[3] TRANSFORMATION PHASE")


    factory_clean = clean_factory(
        factory_df
    )


    product_clean = clean_product(
        product_df
    )


    date_clean = clean_date(
        date_df
    )


    production_clean = clean_production(
        production_df
    )



    # =================================================
    # 4. LOAD PHASE
    # =================================================

    print("\n[4] LOAD PHASE")


    load_factory(
        factory_clean
    )


    load_product(
        product_clean
    )


    load_date(
        date_clean
    )


    load_production(
        production_clean
    )



    # =================================================
    # COMPLETED
    # =================================================


    print("\n" + "=" * 60)

    print(
        "RMG BI AUTOMATION PIPELINE COMPLETED SUCCESSFULLY"
    )

    print("=" * 60)




# =====================================================
# RUN PIPELINE
# =====================================================


if __name__ == "__main__":

    run_pipeline()