# RMG Pipeline Automation

This directory contains the Windows batch script used to execute the
RMG Business Intelligence Automation Pipeline.

## Files

- `run_pipeline.bat`: Executes the Python ETL pipeline.
- `README.md`: Documents the automation process.

## Execution Workflow

The pipeline follows these stages:

1. Extract raw RMG production data.
2. Transform and validate the data.
3. Load the processed data into SQL Server.
4. Record execution results.

## How to Run

From the project root directory, execute:

```cmd
automation\run_pipeline.bat
