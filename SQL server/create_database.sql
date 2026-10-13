

USE master;
GO

IF DB_ID(N'RMG_ANALYTICS') IS NULL
BEGIN
    CREATE DATABASE RMG_ANALYTICS;
    PRINT 'Database RMG_ANALYTICS created successfully.';
END
ELSE
BEGIN
    PRINT 'Database RMG_ANALYTICS already exists; no changes made.';
END;
GO

-- Verify database status
SELECT
    name AS Database_Name,
    state_desc AS Database_Status
FROM sys.databases
WHERE name = N'RMG_ANALYTICS';
GO
