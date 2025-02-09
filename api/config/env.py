import os
from sqlmodel import Session, create_engine

# Get the absolute path of the project root **correctly**
PROJECT_FOLDER = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))  # Moves up two levels
DATABASE_NAME = "Global_Electronics_Retailer.db"
DATABASE_PATH = os.path.join(PROJECT_FOLDER, DATABASE_NAME)  # Ensure DB is in root directory
DATABASE_URL = f"sqlite:///{DATABASE_PATH}"

# Debugging output
print(f"📌 Using DATABASE_PATH: {DATABASE_PATH}")

# Database Connection
CONNECTION_ARGS = {"check_same_thread": False}
ENGINE = create_engine(DATABASE_URL, connect_args=CONNECTION_ARGS)

# Dependency for getting DB session
def get_session():
    with Session(ENGINE) as session:
        yield session