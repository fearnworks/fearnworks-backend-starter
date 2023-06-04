#! /usr/bin/env bash

# Create a new virtual environment
python3 -m venv .venv-test

# Activate the virtual environment
source .venv-test/bin/activate
pip install . 

# Set up test database
export TEST_DATABASE_URL="sqlite:///./test.db"
rm -f ./test.db
alembic upgrade head

# Add app directory to Python path
export PYTHONPATH="$PYTHONPATH:$(pwd)/app"

# Let the DB start
python3 ./app/backend_pre_start.py

# Run migrations on test database
alembic upgrade head --config alembic.ini -x db=test

# Create initial data in test database
python3 ./app/initial_data.py --test