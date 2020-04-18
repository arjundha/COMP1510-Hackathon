# COMP1510-Hackathon

Team 1 for the COMP 1510 Hackathon Final Exam.

| Team Member | Student ID | GitHub ID |
| --- | --- | --- |
| Arjun Dhaliwal | A01207854 | arjundha |
| Hudson McManus | A01190462 | hudsonmcmanus |
| Jessica Hong | A01085702 | jeessicahong |
| Duncan Keen | A01185666 | dkeen10 |

# About our Application
Our application is an all in one tool that Canadian citizens can refer to for receiving the most up
to date information on the COVID-19 crisis. This application can assist you by displaying recent COVID-19
statistics worldwide. 

Upon launching our application (after following the Getting Started steps), the user will be prompted into
generating a User Profile. Shortly after, the user will be welcomed with a plethora of options relating
to COVID-19 information. These options include the following:

1. International COVID-19 Statistics 
2. Information about the user's country (based on current IP address)
3. COVID-19 Statistics on any country the user desires to learn about
4. News articles relating to the COVID-19 crisis (or any topic of interest)
5. Get stock information to see the impact of COID-19 on the world's economy
6. If you are a Canadian citizen, check if you qualify for any form of financial aid.
7. See a chart depicting the pandemic's impact on the DOW

The ip2geotools package is used to determine the user's location based off their IP address, meaning the user does not 
need to enter where they live! The user can input the name of any country and receive that country's stats, or, if they
prefer, they can receive the international scale stats.

The yfinance package is used to provide the user with up to date knowledge on the stock
market. This information can be used to see the impact this pandemic is having on the economy.

The pandas_datareader package is used to create the csv and the data_frame from the created csv.file.

The pandas package is used to read the created dow.csv file.

The matplotlib package is used to plot the data in the data_frame.

Finally, these APIs were used in the development of this application:
1. news.api (https://newsapi.org/)
2. ipify API (https://api.ipify.org/)

# Getting Started
The following steps must be executed before running the application.
In terminal or command line, follow the following steps:
1. Type "git clone https://github.com/arjundha/COMP1510-Hackathon.git"
2. Navigate to your python/Scripts folder
3. Type the following commands to install pip packages:
    1. pip3 install ip2geotools
    2. pip3 install yfinance --upgrade --no-cache-dir
    3. pip3 install pandas
    4. pip3 install pandas_datareader
    5. pip3 install matplotlib
    
    OR
    
    Install the requirements.txt by typing the following:
    1. pip3 install -r requirements.txt
    
4. Run app.py in your Python3 IDE (ex. PyCharm)
5. Now that wasn't so hard, was it?

    
    
# Links
To view our requirements checklist, follow this link: <br>
https://docs.google.com/spreadsheets/d/1JzcajbcolEA8l2ZtXWv04-hl_BFQivgq4AR6XCG9juw/edit?usp=sharing

