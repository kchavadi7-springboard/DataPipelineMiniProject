from DBUtilities import DBUtilities



class DataStatistics:

    def __init__(self):
        self.dbUtility = DBUtilities()


    def event_with_highest_tickets(self, connection=None):
        sql = """SELECT distinct(a.event_name), a.d FROM
(SELECT tps1.ticket_id, tps1.event_name, tps1.num_tickets, SUM(tps1.num_tickets) OVER (PARTITION BY tps1.event_name) as d
FROM third_party_sales as tps1
ORDER BY d desc) a LIMIT 2"""
        # print(sql)
        result = self.dbUtility.executeQuery(sql)
        # print(result)
        flat_list = [str(item) for sublist in result for item in sublist]
        # print(flat_list)
        print('''\n==== The events with highest number of tickets sold ====
---------------------------------------------------------
 Event Name                              Tickets Sold   
---------------------------------------------------------
 {}                        {}
 {}            {}
---------------------------------------------------------
                                 
        '''.format(flat_list[0], flat_list[1], flat_list[2], flat_list[3]))



    def highest_price_events(self):
        sql = """SELECT tps.event_name, tps.price FROM third_party_sales as tps
WHERE tps.price = (SELECT max(tps.price) 
FROM third_party_sales as tps)
GROUP BY tps.event_name"""
        # print(sql)
        result = self.dbUtility.executeQuery(sql)
        # print(result)
        flat_list = [str(item) for sublist in result for item in sublist]
        # print(flat_list)
        print('''\n====     Event tickets sold at highest price     ====
---------------------------------------------------------
 Event Name                              Price Sold At   
---------------------------------------------------------
| {}                        ${}      |
---------------------------------------------------------

        '''.format(flat_list[0], flat_list[1]))




if __name__ == '__main__':
    getStats = DataStatistics()
    getStats.event_with_highest_tickets()
    getStats.highest_price_events()