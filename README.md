# The purpose of this project
  The files involves scraping a website periodically to gather specific information and send it to my Gmail.
# The code
  ## tmp.py
  The main function is the tmp.py file. The file will get browser information by using "urllib request" and "BeutifulSoup" libraries. With the information, the code compares old and new scraped data to identify any changes.
  ## schedule_run.py
  The filecontrols the execution timing of the previous code, with 'tmp' being the main functionality.
  ## my_gmail_account.py
  The file contains the account data for creating another account.
  ## gmail_send.py
  The code sends a gmail to my account using another different created account.
  ## prev_spla
  The folder contains a file where there is the result of tmp.py. The contents of the file will be sent to my gmail account.
