import mysql.connector
import logging

logger = logging.getLogger(__name__)

class DBManager:
    def __init__(self, database='devops_training', host="database", user="root", password=None):
        self.connection = mysql.connector.connect(
            user=user, 
            password=password,
            host=host,
            database=database,
            auth_plugin='mysql_native_password'
        )
        self.cursor = self.connection.cursor()
    
    def populate_db(self):
        logger.info('Populating database with blog posts')
        self.cursor.execute('DROP TABLE IF EXISTS blog')
        self.cursor.execute('CREATE TABLE blog (id INT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(255))')
        self.cursor.executemany('INSERT INTO blog (id, title) VALUES (%s, %s);', [(i, 'Blog post #%d'% i) for i in range (1,5)])
        self.connection.commit()
    
    def query_titles(self):
        logger.debug('Querying blog titles')
        self.cursor.execute('SELECT title FROM blog')
        rec = []
        for c in self.cursor:
            rec.append(c[0])
        return rec
