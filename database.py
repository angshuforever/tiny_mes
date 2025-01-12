from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#POSTGRES_URL = "postgresql://<username>:<password>@<postgress_host_ip>:<port>/<db>"
POSTGRES_URL = "postgresql://<my_user_name>:<password_removed>@localhost:<port_removed>/<db_name_removed>"

engine = create_engine(POSTGRES_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
