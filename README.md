# APOD_Daily_Background

Program takes advantage of NASA's APIs to pull the daily astronomical image of the day and update your windows background. Program works well when you create a batch file and run the task using windows task scheduler.

You must sign up for the nasa api to get the credentials needed for this to work. 

You must replace the credentials for it to work.

In python file: picturescraper.py
replace this path with the path to your folder where pictures will be held.
  PATH = 'C:\\Users\\Rich\\Desktop\\Picture_of_Day\\pic'+d+'.jpg'
  
  replace credentials in following lines.
  key = 'YOUR_KEY_HERE'
  Account_Email = 'YOUR_EMAIL_HERE'
  Account_ID = 'YOUR_ACCOUNT_ID_HERE'
  
  
  
  
 Forgive the poor code this was written a while ago and just had to refresh some of the outdated python and rename paths for a new computer.
