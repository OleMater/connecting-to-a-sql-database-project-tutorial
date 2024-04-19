import os
from sqlalchemy import create_engine
import pandas as pd
from dotenv import load_dotenv

# load the .env file variables
load_dotenv()

# 1) Connect to the database here using the SQLAlchemy's create_engine function
connection_string = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
engine = create_engine(connection_string).execution_options(autocommit=True)
engine.connect()

#########################################
####### CREAT SQL QUERIES BELOW #########
#########################################

results_df = pd.read_sql('''
        SELECT books.title, books.total_pages, books.published_date, publishers.name AS publisher_name
        FROM books JOIN publishers 
        ON publishers.publisher_id = books.publisher_id;
                        ''', engine)
print(results_df)