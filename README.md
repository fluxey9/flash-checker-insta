# Instagram Username Checker Documentation

This script allows you to check the availability of a list of usernames on Instagram in bulk. It utilizes multi-threading for faster checking and can also notify you on Telegram about the availability of usernames.

## Prerequisites

1. Python 3.x is required to run this script.
2. Install the required packages using the following command:
   
   ```bash
   pip install requests cfonts
Have a list of usernames in a text file (users.txt).

1.Clone or download the repository to your local machine.
2.Open a terminal/command prompt and navigate to the script's directory.
3.Run the script using the following command:
  ```bash
python script_name.py
 ```

## Script Features
+Multi-threaded: The script checks usernames using multiple threads for faster processing.
+Telegram Notification: Notifies you on Telegram about the availability of usernames.
+Uses Instagram API: This script uses the Instagram API to check username availability, preventing wrong notifications of banned or deactivated accounts.
+Colorful Output: Utilizes colored text for a visually appealing user interface.

## Configuration
Before running the script, you need to modify the following parts in the script:

Fix, Fix2, and Fix3: These variables contain error messages that the script looks for in the server response. You might need to update them if the Instagram website changes.

URL, headers, and data: These variables contain the necessary information for making requests to the Instagram server. Update them if needed.

##Example Output :
  <   CHECK INSTAGRAM USERNAMES IN BULK  
   <   KEEP USERNAMES IN A TXT FILE IN SAME PATH  
 ---------------------------
 [#] NAME       : KARAN
 [#] WEBSITE    : https://karan.vip
 [#] INSTAGRAM  : @56536
 [#] TELEGRAM   : anarchs
 ---------------------------
...
[Username ~ Error] ==> username_error
[Username ~ TaKen] ==> username_taken
[Username ~ Good] ==> username_good
...



