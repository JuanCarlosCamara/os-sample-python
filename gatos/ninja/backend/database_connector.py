import config as CFG
import pandas as pd
import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DatabaseConnector(object):
    def __init__(self):
        self.conn = create_engine(
            'postgresql://' + CFG.DB_USER + ':' + CFG.DB_PASS +
            '@' + CFG.DB_HOST + ':' + CFG.DB_PORT + '/' + CFG.DB_DATABASE)

    def read_query(self, query):
        logging.debug('Reading from database query: ' + query)
        df = pd.read_sql_query(query, self.conn)
        logging.debug('Total records read = ' + str(df.shape[0]))

        return df

    def read_query_by_chunks(self, query, chunksize):
        logging.debug('Reading from database query by chunks: ' + query)
        chunk = pd.read_sql_query(query, self.conn, chunksize=chunksize)
        # logging.debug('Total records read = ' + str(chunk.shape[0]))

        return chunk

    def write_query(self, tablename, df):
        df.to_sql(tablename, self.conn, schema=CFG.SCALIDAD_SCHEMA, if_exists='replace', index=False)
        logging.debug(str(df.shape[0]) + ' records inserted in table ' + tablename)

    def write_query_by_chunks(self, tablename, df, chunksize):
        df.to_sql(tablename, self.conn, schema=CFG.SCALIDAD_SCHEMA, if_exists='append', index=False,
                  chunksize=chunksize)

        logging.debug(str(df.shape[0]) + ' records inserted in table ' + tablename)

    def exec_statement(self, statement):
        logging.debug('Executing statement {0}'.format(statement))

        Session = sessionmaker(bind=self.conn)
        session = Session()
        session.execute(statement)
        session.commit()
        session.close()

    def drop_table(self, table):
        statement = 'DROP TABLE IF EXISTS {0}."{1}"'.format(CFG.SCALIDAD_SCHEMA, table)

        self.exec_statement(statement)

        logging.info('Table ' + table + ' has been dropped')

    def truncate_table(self, table):
        statement = 'TRUNCATE TABLE {0}."{1}"'.format(CFG.SCALIDAD_SCHEMA, table)

        self.exec_statement(statement)

        logging.info('Table ' + table + ' has been truncated')

    def close(self):
        self.conn.dispose()
