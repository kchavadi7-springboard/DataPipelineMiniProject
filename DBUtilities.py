import mysql.connector
from constants import USER, PASSWORD, HOST, PORT, DATABASE
from csv import reader, DictReader
import datetime



class DBUtilities:
    def __init__(self):
        pass


    def get_db_connection(self):
        connection = None
        try:
            connection = mysql.connector.connect(user=USER,
                                                 password=PASSWORD,
                                                 host=HOST,
                                                 port=PORT,
                                                 database=DATABASE
            )
            print("Connection Successful !!!")
        except Exception as error:
            print("Error while connecting to database for job tracker", error)

        return connection

    #####################################################################################################
    # CREATE TABLE: third_party_sales

    def createTable(self):
        try:
            sql = """CREATE TABLE IF NOT EXISTS third_party_sales(
    ticket_id INT,
    trans_date VARCHAR(50),
    event_id INT,
    event_name VARCHAR(50),
    event_date DATE,
    event_type VARCHAR(10),
    event_city VARCHAR(20),
    customer_id INT,
    price DECIMAL,
    num_tickets INT
    )"""
            # print(sql)
            self.executeQuery(sql)
            print("\nCREATED TABLE SUCCESSFULLY !!!\n")
        except Exception as error:
            print("Could not create table! ")

    #####################################################################################################
    # GET TABLE COLUMN NAMES

    def getMySQLColumnNames(self):
        table_query = "SHOW TABLES"
        tablename_query = self.executeQuery(table_query)
        for i in tablename_query[0]:
            table_name = i
        print("\nTable selected to insert data: ",table_name, "\n")
        query = """SELECT COLUMN_NAME
                                   FROM INFORMATION_SCHEMA.COLUMNS
                                   WHERE TABLE_SCHEMA = 'Tickets' AND TABLE_NAME = '{}'
                                   ORDER BY ORDINAL_POSITION""".format(table_name)
        # print(query)
        column_names = self.executeQuery(query)
        column_list = list(map(list, column_names))
        flat_list = [item for sublist in column_list for item in sublist]
        result = tuple(flat_list)
        return result

    #####################################################################################################
    # CONVERT TABLE NAMES
    def convertListToString(self, sentList):
        result = ""
        for row in sentList:
            result += row + ","
        result = result[:-1]
        return result

    #####################################################################################################
    # CONVERT COLUMN LIST TO string

    def convertListToQuotedString(self, sentList):
        result = ""
        for row in sentList:
            result += self.checkValue(row) + ","
        result = result[:-1]
        return result

    def checkValue(self, value):
        if type(value)  == type("hello"):
            return "'{}'".format(value.replace("'","''"))      #repr(value)
        elif type(value) == type(None):
            return '{}'.format("NULL")#"''"
        elif type(value) == type(7):
            return '{}'.format(value) #str(value)
        elif type(value) == type(7.9):
            return '{}'.format(value) #str(value)
        elif type(value) == type(datetime.datetime(2019, 1, 3, 15, 27, 18)):
            return "'{}'".format(value) #"'" +str(value)+ "'"
        else:
            print("Could not find" + str(type(value)) + " for value " +str(value))
            return "'{}'".format(value) #str(value)

    #####################################################################################################
    # QUERY EXECUTION
    def executeQuery(self, query):
        db = self.get_db_connection()
        cursor = db.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        db.close()
        return result




if __name__ == '__main__':
    getConnect = DBUtilities()
    # coln = getConnect.getMySQLColumnNames()
    # getConnect.convertListToString(coln)
    # getConnect.get_db_connection()
    getConnect.createTable()