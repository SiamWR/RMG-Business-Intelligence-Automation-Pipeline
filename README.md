# RMG Business Intelligence Automation Pipeline

An end-to-end Business Intelligence and automation project designed to transform raw Ready-Made Garment (RMG) production data into structured business insights and automated management reports.

The project integrates **Python, SQL Server, Power BI, Power Automate, and Windows Task Scheduler** to demonstrate a complete data-to-insight workflow.


## 📌 Project Overview

The Ready-Made Garment (RMG) industry generates production data across factories, products, production targets, output, defects, and operational performance.

Manually processing this information can be time-consuming and can introduce inconsistencies in reporting.

This project develops an automated BI pipeline that processes production data through multiple stages:


Raw Production Data
        │
        ▼
Python Data Generation / Extraction
        │
        ▼
Data Cleaning & Transformation
        │
        ▼
SQL Server Database
        │
        ▼
Power BI Data Model
        │
        ▼
Interactive Power BI Dashboard
        │
        ▼
Power BI PDF Report Export
        │
        ▼
Power Automate
        │
        ▼
Automated Report Distribution

## Structure
                    
RMG-Business-Intelligence-Automation-Pipeline/
│
├── automation/
│   └── run_pipeline.bat
│
├── python/
│   ├── check_data.py
│   ├── check_date.py
│   ├── config.py
│   ├── extract.py
│   ├── generate_data.py
│   ├── load.py
│   ├── pipeline.py
│   ├── test_sql.py
│   ├── test_transform.py
│   └── transform.py
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── errors/
│
├── sql/
│   └── SQL scripts
│
├── powerbi/
│   └── Power BI files and related assets
│
├── documentation/
│   └── Project documentation
│
├── .gitignore
│
└── README.md

                    ┌──────────────────────────┐
                    │    Raw RMG Data          │
                    │ Factory / Product /      │
                    │ Date / Production        │
                    └────────────┬─────────────┘
                                 │
                                 ▼
                    ┌──────────────────────────┐
                    │       Python ETL         │
                    │                          │
                    │ Extract                  │
                    │ Transform                │
                    │ Validate                 │
                    │ Load                     │
                    └────────────┬─────────────┘
                                 │
                                 ▼
                    ┌──────────────────────────┐
                    │       SQL Server         │
                    │      RMG_ANALYTICS       │
                    │                          │
                    │ dim_factory              │
                    │ dim_product              │
                    │ dim_date                 │
                    │ fact_production          │
                    └────────────┬─────────────┘
                                 │
                                 ▼
                    ┌──────────────────────────┐
                    │        Power BI          │
                    │                          │
                    │ Data Model               │
                    │ Measures                 │
                    │ KPIs                     │
                    │ Interactive Dashboard    │
                    └────────────┬─────────────┘
                                 │
                                 ▼
                    ┌──────────────────────────┐
                    │    PDF Report Export     │
                    └────────────┬─────────────┘
                                 │
                                 ▼
                    ┌──────────────────────────┐
                    │     Power Automate       │
                    │                          │
                    │ Scheduled Workflow       │
                    │ Report Processing        │
                    │ Distribution             │
                    └──────────────────────────┘
