from DBUtilities import DBUtilities
from DataInsertion import DataInsertion
from DataStatistics import DataStatistics



class main:
    def __init__(self):
        self.dbUtility = DBUtilities()
        self.dataInsertion = DataInsertion()
        self.dataStats = DataStatistics()


    def runProgram(self):
        self.dbUtility.createTable()
        self.dataInsertion.load_third_party_data()
        self.dataStats.event_with_highest_tickets()
        self.dataStats.highest_price_events()




if __name__ == '__main__':
    mainV = main()
    mainV.runProgram()
