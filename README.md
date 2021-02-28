# DataPipelineMiniProject
This project illustrates on loading small dataset from csv to MySQL database

This project will:
>* Connect to your database
>* Create a ```third_party_sales``` table in your database
>* Load the ```third_party_sales_1.csv``` file i.e. the data provided by Springboard into the ```third_party_sales``` table created by this code
>* Get few of the possible analytics gathered from the data 





## To get step by step process that is happening in Data Pipeline follow below instructions:


After downloading the project
1) Set your database credentials
* Replace the database variables(USER, PASSWORD, HOST, PORT, DATABASE) with your database information where you would want the table: third_party_sales to be created

2) Create table 'third_party_sales' in your db selected:
* ```Run DBUtilities.py file```

3) Load csv data into the table 'third_party_sales' created
* ```Run DataInsertion.py file```

4) To get the possible analytics information from the data
* ```Run DataStatistics.py file```




## To run entire program in one go and right away get analytics information:
* ```Just run the main.py file```














