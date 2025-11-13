import mysql.connector
import logging

logger = logging.getLogger(__name__)


class DBManager:
    # def __init__(self, database='devops_training', host="database", user="root", password=None):
    #     self.connection = mysql.connector.connect(
    #         user=user,
    #         password=password,
    #         host=host,
    #         database=database,
    #         auth_plugin='mysql_native_password'
    #     )
    #     self.cursor = self.connection.cursor()
    def __init__(self):
        pass

    def populate_db(self):
        logger.info("Populating database with blog posts")
        # self.cursor.execute('DROP TABLE IF EXISTS blog')
        # self.cursor.execute('CREATE TABLE blog (id INT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(255))')
        # self.cursor.executemany('INSERT INTO blog (id, title) VALUES (%s, %s);', [(i, 'Blog post #%d'% i) for i in range (1,5)])
        # self.connection.commit()
        with open("db.txt", "w") as f:
            f.write("First Blog Post\n")
            f.write("Another Day, Another Post\n")
            f.write("Flask is Awesome\n")

    def query_titles(self):
        # logger.debug('Querying blog titles')
        # self.cursor.execute('SELECT title FROM blog')
        # rec = []
        # for c in self.cursor:
        #     rec.append(c[0])
        with open("db.txt", "r") as f:
            rec = [line.strip() for line in f.readlines()]
        return rec

    def append_title(self, title):
        logger.debug("Appending new blog title: %s", title)
        # self.cursor.execute('INSERT INTO blog (title) VALUES (%s);', (title,))
        # self.connection.commit()
        with open("db.txt", "a") as f:
            f.write(title + "\n")

    def close(self):
        logger.debug("Closing database connection")
        # self.cursor.close()
        # self.connection.close()
        pass

if __name__ == "__main__":
    db = DBManager()
    db.populate_db()
    titles = db.query_titles()
    print("Blog Titles:", titles)
    db.append_title("New Blog Post")
    titles = db.query_titles()
    print("Updated Blog Titles:", titles)
    db.close()
