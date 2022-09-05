# Instructions

1.  Clone the repository

2.  Install all required packages from the Pipfile

3.  Create a file called config.py in the api directory and enter your two API keys as follows:

        rankings_api_key = {YOUR_SCOREBOARD_API_KEY}
        scoreboard_api_key = {YOUR_RANKINGS_API_KEY}

4.  Navigate to the api directory on your comman line and enter the following command:

        uvicorn main:app

5.  Open a web browser and navigate to http://127.0.0.1:8000/results?datefrom=YYYY-MM-DD&dateto=YYYY-MM-DD&apikey=resulta

6.  Enjoy!. I have added a .txt file with my thought process in this repository as requested.
