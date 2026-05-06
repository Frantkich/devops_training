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

    def query_titles(self):
        logger.debug('Querying blog titles')
        self.cursor.execute('SELECT title FROM blog')
        rec = [c[0] for c in self.cursor.fetchall()]
        return rec

    def append_title(self, title):
        logger.debug("Appending new blog title: %s", title)
        self.cursor.execute('INSERT INTO blog (title) VALUES (%s);', (title,))
        self.connection.commit()

    def close(self):
        logger.debug("Closing database connection")
        self.cursor.close()
        self.connection.close()
        pass
