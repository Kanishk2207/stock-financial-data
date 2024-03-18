To Run the applcation.

1. From Run and Debug - Create new launch.json file, select FastAPI and save this file without any changes.
2. Now we can run our application using this setup always.

-- make a db instance and change the db environment variable in .env file if not creating docker image of mysql

To Run the application through docker image

1. Run the below command from the root directory which would create the docker image.
   docker compose up --build (use --build only on first time)

**RECOMMENDED TO RUN THROUGH DOCKER IMAGE**

-- after creating the docker image of mysql, open the mysql(through cli or workbench) and create following table:

"
Table: financial_data

Columns:
id int AI PK
ticker varchar(50)
date date
revenue bigint
gp bigint
fcf bigint
capex bigint
"
