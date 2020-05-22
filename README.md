# Data Warehouse 98point6

This utility extracts data related to the 98point6 Drop Token game and its players from external sources, transforms the data where appropriate, and loads it into a local SQL Server database.

**Game Data Source**: https://s3-us-west-2.amazonaws.com/98point6-homework-assets/game_data.csv
**Player Data Source**: https://x37sv76kth.execute-api.us-west-1.amazonaws.com/prod/users

### Software Requirements:
1. Locally installed [SQL Server] (https://docs.microsoft.com/en-us/sql/database-engine/install-windows/install-sql-server?view=sql-server-ver15)
2. [SQL Server Management Studio] (https://docs.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms?view=sql-server-ver15)
3. Python 3 (See requirements.txt file for required packages, all of which can be installed via pip)

### Info About Directories in this Package
- **Internal data_warehouse_98point6 directory**: contains all of the main execution code.
- **db**: Scripts to generate the database schema. Files follow a db_script_<SQL Server Version>.sql naming convention.
- **config**: Specifies connection info for the local SQL Server/database.

### Steps to Setup Your System
1. In the config directory, create a copy of db_connection.ini.template and rename it db_connection.ini. Replace the value "<Server_Name>" with the name of your local server. This will be the same as the server name specified in SQL Server Management Studio.
2. In the db directory, open the file matching your SQL Server version and execute it in SQL Server Management Studio. This will stage the database.

## Executing the Utility
1. Open a command window within the main directory (the directory containing main.py).
2. At the command-line, type "python main"
3. Type the number indicating the mode of the utility you would like to run. "1" will load all game and player data. "2" will only load player data that had previously failed (stored in errors/player_errors.json)