# SuperchargingDevelopersDemo

## Build and run containers
```
docker-compose up -d --build
```
_Remove "-d" if you want to launch the app in current terminal session._
## Application start
Run app:
```
docker-compose up -d
```

Verify if http://localhost:8000/healthcheck returns `{"status":"ok"}`. 

Verify database connection `jdbc:postgresql://localhost:5432/app`. 

Shut down app:
```
docker-compose down
```

Format code:
```
docker compose exec app format

# if the container is not running
docker compose run app format
```

## Database migrations
### Create a new migration
When you need to add a new table, import its metadata to "metadata" list variable in `src/databases.py`. 
The example can be seen here `src/auth/models.py`. 
```
docker compose exec app makemigrations *migration_name*
```
This will create a new migration file with new tables detected
### Init or edit schema
This will execute all alembic migrations in `alembic/versions/...`.
Run it every time you need to create or update the schema.
```
docker compose exec app migrate
```

### Downgrade migrations
This will downgrade schema to the previous version. You can provide a number of "steps back" 
or a hash of the specific version.
```
docker compose exec app downgrade -1  # or -2 or base or hash of the migration
```