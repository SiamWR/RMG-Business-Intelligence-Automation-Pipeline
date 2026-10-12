# RMG Business Intelligence Automation Pipeline

An end-to-end Business Intelligence and automation project designed to transform raw Ready-Made Garment (RMG) production data into structured business insights and automated management reports.

The project integrates **Python, SQL Server, Power BI, Power Automate, and Windows Task Scheduler** to demonstrate a complete data-to-insight workflow.


## Project Overview

The Ready-Made Garment (RMG) industry generates production data across factories, products, production targets, output, defects, and operational performance.

Manually processing this information can be time-consuming and can introduce inconsistencies in reporting.

This project develops an automated BI pipeline that processes production data through multiple stages:

```text
Raw Production Data
        ↓
Python ETL Pipeline
        ↓
Data Cleaning & Validation
        ↓
SQL Server
        ↓
Power BI
        ↓
Interactive Dashboard
        ↓
PDF Report Export
        ↓
Power Automate
        ↓
Automated Report Distribution
```

## Objectives

- Build an end-to-end BI pipeline for RMG production data
- Generate realistic synthetic production data for development and testing
- Automate data extraction, transformation, validation, and loading
- Store structured production data in SQL Server
- Develop production performance KPIs
- Build an interactive Power BI dashboard
- Automate report generation and distribution
- Schedule pipeline execution using Windows Task Scheduler
- Maintain the project using Git and GitHub

---

## Technology Stack

| Technology | Purpose |
|---|---|
| **Python** | Data generation, extraction, transformation, validation, and orchestration |
| **Pandas** | Data manipulation and transformation |
| **Faker** | Synthetic business data generation |
| **PyODBC** | Python–SQL Server connectivity |
| **SQL Server** | Central relational database |
| **SQL** | Database operations and analytical queries |
| **Power BI** | Business intelligence and visualization |
| **Power Automate** | Workflow and reporting automation |
| **Windows Task Scheduler** | Scheduled pipeline execution |
| **Git** | Version control |
| **GitHub** | Source-code hosting and documentation |
| **VS Code** | Development environment |

---

## System Architecture

The project follows a layered architecture connecting data processing, database management, business intelligence, and automation.

```text
┌─────────────────────────────────────────────────────────────┐
│                    DATA SOURCE LAYER                        │
│                                                             │
│                 RMG Production Data                         │
│                                                             │
│    Factory | Product | Date | Production | Target | Defect  │
└─────────────────────────────┬───────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                     PYTHON ETL LAYER                        │
│                                                             │
│             Extract → Transform → Validate → Load           │
│                                                             │
│       Data Cleaning | Transformation | KPI Preparation      │
└─────────────────────────────┬───────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                    DATABASE LAYER                            │
│                                                             │
│                      SQL Server                             │
│                    RMG_ANALYTICS                             │
│                                                             │
│  dim_factory | dim_product | dim_date | fact_production     │
└─────────────────────────────┬───────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│               BUSINESS INTELLIGENCE LAYER                   │
│                                                             │
│                       Power BI                               │
│                                                             │
│     Data Model | Measures | KPIs | Dashboard | Filters      │
└─────────────────────────────┬───────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                    REPORTING LAYER                          │
│                                                             │
│                  Power BI PDF Export                         │
└─────────────────────────────┬───────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                    AUTOMATION LAYER                         │
│                                                             │
│                    Power Automate                            │
│                                                             │
│              Report Processing & Distribution                │
└─────────────────────────────────────────────────────────────┘
