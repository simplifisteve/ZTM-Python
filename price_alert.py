import requests
import smtplib
import time

ITAD_API_KEY = 'your_api_key'

def check_price():
    url = f'https://api.isthereanydeal.com/v02/game/prices/?key={ITAD_API_KEY}&plains=steam&game_id=916440'

    response = requests.get(url, timeout=5)
    data = response.json()
    
    current_price = data['data']['list'][0]['price_new']
    
    if current_price < 59.99: # sale threshold price
        send_email()

def send_email():

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    
    server.login('your_email@gmail.com', 'your_password')
    
    subject = 'Anno 1800 Complete Edition is on sale!'
    body = 'Check it out! Game is on sale: https://isthereanydeal.com/game/annoiviii00completeeditionyeariv/history/'  
    
    msg = f"Subject: {subject}\n\n{body}"
    
    server.sendmail(
        'from_email@gmail.com',
        'to_email@gmail.com',
        msg
    )
    print('Email sent!')

while True:
    check_price()
    time.sleep(86400) # Check daily

# # To use with Beautiful Soup
# import requests
# import smtplib
# import time

# url = 'https://isthereanydeal.com/game/annoiviii00completeeditionyeariv/history/'

# def check_price():
#     page = requests.get(url)
#     soup = BeautifulSoup(page.content, 'html.parser')

#     price = soup.find("td", {"class": "price"}).text.strip()

#     if float(price) < 59.99: 
#         print("Anno 1800 Complete Edition is on sale!")
#         send_email()
#     else:
#         print("Anno 1800 Complete Edition is not on sale")

# def send_email():
#     # Send email code 

# while True:
#     check_price()
#     time.sleep(86400) 
