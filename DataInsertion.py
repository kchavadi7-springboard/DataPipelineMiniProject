import mysql.connector
from constants import CSV_FILE_PATH
from csv import reader, DictReader
import datetime
from DBUtilities import DBUtilities


class DataInsertion:
    def __init__(self):
        self.dbUtility = DBUtilities()


    def load_third_party_data(self, connection=None, file_path_csv=None):
        connection = self.dbUtility.get_db_connection()
        cursor = connection.cursor()
        # iterate through the csv file and execute insert statement
        tables = self.dbUtility.getMySQLColumnNames()
        table_names = self.dbUtility.convertListToString(tables)
        # print(table_names)

        with open(CSV_FILE_PATH, 'r') as file_obj:
            csv_reader = reader(file_obj)
            for row in csv_reader:
                val = self.dbUtility.convertListToQuotedString(row)
                sql = """INSERT INTO third_party_sales ({}) VALUES ({})""".format(table_names, val)
                print(sql)
                cursor.execute(sql)
                connection.commit()
                result = cursor.fetchall()
                print("Inserted row successfully!\n")
        cursor.close()
        return





if __name__ == '__main__':
    dataInsert = DataInsertion()
    dataInsert.load_third_party_data()