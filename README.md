# Campaign Contributions ETL Project

The **Campaign ETL Project** is a data engineering project that extracts American candidate/recipient data spanning 1979-2024 from a CSV file, transforms it into a clean SQL schema, and loads it into **PostgreSQL** for analysis.

Built with **Dagster** for orchestration and **pgAdmin4** for database management.

Data Source: **dime_recipients_1979_2024.csv.gz - Candidate/Recipient CFscores** at https://data.stanford.edu/dime

## Features

- **Extracts, Transforms, and Loads** raw candidate/recipient data from CSV, transforms datatypes, and loads it into PostgreSQL tables for further use.
- **Orchestration** via Dagster.
- **Database inspection** via pgAdmin4.

## Setup Instructions

### 1. Clone Repository
git clone https://github.com/joshua-candra/campaign-etl-project.git

cd campaign-etl-project

### 2. Install Python Dependencies
pip install -r requirements.txt

### 3. Configure Environment Variables
Before running, create an '.env' file with the following line of PostgreSQL details. The default port number in PostgreSQL is 5432.

DATABASE_URL=postgresql://username:password@localhost:5432/campaign_db

### 4. Create Database in PostgreSQL
In pgAdmin4, create a new database called "campaign_db", then run the below command in the terminal:

psql -h localhost -U postgres -d campaign_db -f sql/create-tables.sql

### 5. Run Dagster
To run, use the below command in the terminal while location is at campaign-etl-project:

dagster dev -m campaign_dagster.definitions

Open Dagster using the link (http://127.0.0.1:3000/assets) and materialize all assets.

If you get an error saying that a relation/table does not exist, manually run the SQL query from create-tables.sql in your SQL editor (pgAdmin/Workbench).
