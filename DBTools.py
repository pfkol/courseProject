import psycopg2


class DB:
    connection = psycopg2.connect(user="postgres", password="postgres", host="127.0.0.1", port="5432", database="test")
    connection.autocommit = False

    def dbInsertProducts(self, records):
        try:
            cursor = self.connection.cursor()
            sqlInsert = "INSERT INTO pk.products (id, name, year, color, pantone_value) VALUES (%s,%s,%s,%s,%s)"
            result = cursor.executemany(sqlInsert, records)
            print(cursor.rowcount, "Record inserted successfully into mobile table")
        except Exception as err:
            self.connection.rollback()
        finally:
            if(self.connection):
                self.connection.commit()
                cursor.close()
                self.connection.close()
                print("Conn to Postgres was closed")



