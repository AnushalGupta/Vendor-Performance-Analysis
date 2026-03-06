import pandas as pd
import os
from sqlalchemy import create_engine
import logging
import time

engine = create_engine('sqlite:///inventory.db')

def ingest_db(df, table_name, engine):
    '''this function will ingest the dataframe into database table'''
    df.to_sql(table_name,con =engine,if_exists = 'replace' ,index =False,chunksize=100000)

def load_raw_data(): 
    '''this function will load CSV files as dataframe and ingest into db'''
    start = time.time()
    for file in os.listdir('data'):
        if file.endswith('.csv'):  
            file_path = os.path.join('data', file)
            df = pd.read_csv(file_path)
            logging.info(f'ingesting {file} in db')
            ingest_db(df, file[:-4], engine)
    end = time.time()
    logging.info('--------------Ingestion Complete--------------')
    logging.info(f'Total time taken to ingest : {(end-start)/60}')

if __name__ == '__main__':
    logging.basicConfig(
    	filename = 'logs/ingestion_db.log',
    	level = logging.DEBUG,
    	format="%(asctime)s - %(levelname)s- %(message)s",
    	filemode="a"
    )
    load_raw_data()
