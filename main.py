import requests
import threading
from cfonts import render
from random import choice

try:
    from cfonts import render
except ImportError:
    print("Please install missing libraries: cfonts")

W = "\033[0m"
G = '\033[32;1m'
R = '\033[31;1m'
A = "\033[1;91m"
B = "\033[1;90m"
C = "\033[1;97m"
E = "\033[1;92m"
H = "\033[1;93m"
K = "\033[1;94m"
L = "\033[1;95m"
M = "\033[1;94m"

Fix = '{"message":"feedback_required","spam":true,"feedback_title":"Try Again Later","feedback_message":"We limit how often you can do certain things on Instagram to protect our community. Tell us if you think we made a mistake.","feedback_url":"repute/report_problem/scraping/","feedback_appeal_label":"Tell us","feedback_ignore_label":"OK","feedback_action":"report_problem","status":"fail"}'
Fix2 = '"errors": {"username":'
Fix3 = '"code": "username_is_taken"'

def Banner():
    Bannerx = f""" {C}<   {H}                           {C}>"""
    output = render('FLASH CHECKER', colors=[str(choice(['red', 'cyan', 'magenta', 'blue', 'yellow'])), str(choice(['cyan', 'magenta', 'blue', 'yellow', 'red'])), str(choice(['magenta', 'blue', 'yellow', 'red', 'cyan']))], align='left', space='0')

    Banner = f"""
  {C}<   {H}CHECK INSTAGRAM USERNAMES IN BULK {C}>  
   {C}<   {H}KEEP USERNAMES IN A TXT FILE IN SAME PATH {C}> 
 {C}---------------------------
 {R}[{C}#{R}] {H}NAME       {C}: {H}KARAN
 {R}[{C}#{R}] {H}WEBSITE    {C}: {H}https://karan.vip
 {R}[{C}#{R}] {H}INSTAGRAM  {C}: {H}@56536
 {R}[{C}#{R}] {H}TELEGRAM   {C}: {H}anarchs
 {C}---------------------------"""
    print(output + Bannerx + Banner)

def Check(username):
    URL = f"https://www.instagram.com/accounts/web_create_ajax/attempt/"
    headers = {'Host':'www.instagram.com', 'content-length':'85', 'sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="101"', 'x-ig-app-id':'936619743392459', 'x-ig-www-claim':'0', 'sec-ch-ua-mobile':'?0', 'x-instagram-ajax':'81f3a3c9dfe2', 'content-type':'application/x-www-form-urlencoded', 'accept':'/', 'x-requested-with':'XMLHttpRequest', 'x-asbd-id':'198387', 'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Safari/537.36', 'x-csrftoken':'jzhjt4G11O37lW1aDFyFmy1K0yIEN9Qv', 'sec-ch-ua-platform':'"Linux"', 'origin':'https://www.instagram.com', 'sec-fetch-site':'same-origin', 'sec-fetch-mode':'cors', 'sec-fetch-dest':'empty', 'referer':'https://www.instagram.com/accounts/emailsignup/', 'accept-encoding':'gzip, deflate, br', 'accept-language':'en-IQ,en;q=0.9', 'cookie':'csrftoken=jzhjt4G11O37lW1aDFyFmy1K0yIEN9Qv', 'cookie':'mid=YtsQ1gABAAEszHB5wT9VqccwQIUL', 'cookie':'ig_did=227CCCC2-3675-4A04-8DA5-BA3195B46425', 'cookie':'ig_nrcb=1'}
    data = f'email=aakmnnsjskksmsnsn%40gmail.com&username={username}&first_name=&opt_into_one_tap=false'
    response = requests.post(url=URL, headers=headers, data=data)

    if Fix in response.text:
        print(f"{R}[{C}Username ~ Error{R}] {C}==> {R}{username}")
    elif Fix2 in response.text:
        print(f"{R}[{C}Username ~ TaKen{R}] {C}==> {R}{username}")
    elif Fix3 in response.text:
        print(f"{R}[{C}Username ~ TaKen{R}] {C}==> {R}{username}")
    else:
        with open("Available.txt", "a") as file:
            file.write(f"{username}\n")

        requests.post(f'https://api.telegram.org/bot{TokeN}/sendMessage?chat_id={iD}&text=Username ✓ : {username}')
        print(f"{R}[{C}Username ~ Good{R}] {C}==> {E}{username}")

if __name__ == "__main__":
    Banner()
    iD = input(f" {R}[{C}+{R}] {C}TELEGRAM ID {R}: ")
    TokeN = input(f" {R}[{C}+{R}] {C}BOT API-AUTH TOKEN {R}: ")
    filename = input(f" {R}[{C}+{R}] {C}PATH/FILE NAME TO CHECK {R}: ")
    with open(filename) as f:
        usernames = f.readlines()
    usernames = [username.strip() for username in usernames]

    threads = []
    for username in usernames:
        thread = threading.Thread(target=Check, args=(username,))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()
