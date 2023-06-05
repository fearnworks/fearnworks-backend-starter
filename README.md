# fearnworks-backend-starter
 A backend project with fastapi, auth, db, and alembic. Meant to be deployed through docker. 
 
 To run :
 
 ```bash 
 git clone https://github.com/fearnworks/fearnworks-backend-starter.git
 cd fearnworks-backend-starter
 cp backend/app/.envtemplate backend/app/.env
 chmod +x backend/app/run.sh
 docker-compose up
 ```

Depending on your environment permissions you might need sudo for the docker-compose. 

Then navigate to the endpoint in the logs

## API Endpoints
The application provides several starter API endpoints, including:

/: The root endpoint, which returns an HTML page.
/ping: A simple endpoint for checking the application status. It returns {"ping": "pong!"}.
/docs : FASTApi Swagger style api explorer

## Database Migrations
The project uses Alembic for handling database schema changes. The alembic directory contains the migration scripts and configuration for Alembic.

Before running the migrations, make sure your database connection is correctly configured in the environment variables.

To run database migrations, you would typically follow these steps:

1. Initialization: If you are setting up Alembic for the first time, you would need to initialize it. However, this project already includes an initialized Alembic setup, so you can skip this step.

2. Generate a Migration Script: After you make changes to your SQLAlchemy models, you can auto-generate a migration script with the following command:

```bash
alembic revision --autogenerate -m "Your message"
```

Replace "Your message" with a brief description of the changes made. This command will create a new migration script in the alembic/versions directory.

3. Review the Migration Script: It's important to review the auto-generated script to make sure it includes the desired changes and doesn't include any unwanted changes. Alembic can typically handle adding tables and columns, but more complex migrations (like column renaming or data transformations) might need to be written manually.

4. Run the Migrations: After you are satisfied with the migration script, you can apply the migrations with the following command:

```bash

alembic upgrade head
```
This command will apply all migrations up to the "head" (the latest migration).

### Downgrading Migrations: 
If you need to undo a migration, you can downgrade one revision with the following command:

```bash
alembic downgrade -1
```
Replace -1 with the number of revisions you want to downgrade, or use a specific revision number instead of -1 to downgrade to that revision.

Remember, Alembic is a powerful tool, but it isn't magic. Always review your migration scripts and test them in a safe environment before applying them to your production database.

## Security and Authentication
The project uses bcrypt for password hashing and verification, and JWT for user authentication and access token management.

- The auth.py file in the core module handles user authentication and token management. It includes functions for user authentication and the creation of access tokens.
- The security.py file in the core module handles password encryption and verification using bcrypt. It includes functions for verifying a password against a hashed password and hashing a password.

## Set up Commands : 
To determine the ip of docker-compose host : 

```bash
sudo apt install net-tools
ifconfig | grep "inet " | grep -Fv 127.0.0.1 | awk '{print $2}'
```


## License 

This project is licensed under the terms of the Apache 2.0 License 
