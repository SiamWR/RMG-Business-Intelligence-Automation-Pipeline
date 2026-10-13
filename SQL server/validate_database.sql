

USE RMG_ANALYTICS;
GO

-- Confirm that all expected tables exist before running row-count queries.
IF OBJECT_ID(N'dbo.dim_factory', N'U') IS NULL
    THROW 50001, 'Required table dbo.dim_factory was not found. Run the Python pipeline first.', 1;

IF OBJECT_ID(N'dbo.dim_product', N'U') IS NULL
    THROW 50002, 'Required table dbo.dim_product was not found. Run the Python pipeline first.', 1;

IF OBJECT_ID(N'dbo.dim_date', N'U') IS NULL
    THROW 50003, 'Required table dbo.dim_date was not found. Run the Python pipeline first.', 1;

IF OBJECT_ID(N'dbo.fact_production', N'U') IS NULL
    THROW 50004, 'Required table dbo.fact_production was not found. Run the Python pipeline first.', 1;
GO

-- 1. Count factory records
SELECT COUNT(*) AS Factory_Count
FROM dbo.dim_factory;
GO

-- 2. Count product records
SELECT COUNT(*) AS Product_Count
FROM dbo.dim_product;
GO

-- 3. Count calendar/date records
SELECT COUNT(*) AS Date_Count
FROM dbo.dim_date;
GO

-- 4. Count production records
SELECT COUNT(*) AS Production_Count
FROM dbo.fact_production;
GO

-- 5. Inspect up to 10 production records
-- This assumes Production_ID is present in fact_production.
SELECT TOP (10) *
FROM dbo.fact_production
ORDER BY Production_ID DESC;
GO

-- 6. Optional: inspect table names and approximate row counts in dbo schema
SELECT
    s.name AS Schema_Name,
    t.name AS Table_Name,
    SUM(p.rows) AS Approximate_Row_Count
FROM sys.tables AS t
JOIN sys.schemas AS s
    ON s.schema_id = t.schema_id
JOIN sys.partitions AS p
    ON p.object_id = t.object_id
WHERE s.name = N'dbo'
  AND p.index_id IN (0, 1)
  AND t.name IN (N'dim_factory', N'dim_product', N'dim_date', N'fact_production')
GROUP BY s.name, t.name
ORDER BY t.name;
GO
