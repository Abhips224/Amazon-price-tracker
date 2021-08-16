
import urllib.request
import bs4
import smtplib
import time

price_list=[]
def check_price():
    url="https://www.amazon.in/dp/B08S5CGQ9K/ref=sspa_dk_detail_0?psc=1&pd_rd_i=B08S5CGQ9K&pd_rd_w=SEJ78&pf_rd_p=3d347ba3-873a-4950-a530-1b4d5938343e&pd_rd_wg=6g0rO&pf_rd_r=QNV9YWS2EVAHRFYRSVX4&pd_rd_r=3d354e82-66ad-48fe-9a46-aaabdb2b22bc&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzMlRMSTlQSEpWWTIxJmVuY3J5cHRlZElkPUEwMTc4MTk0MVIwUTcwSks4TVc2SCZlbmNyeXB0ZWRBZElkPUEwNjQ2NDcyM1FJNkgxNE1DM1RMOSZ3aWRnZXROYW1lPXNwX2RldGFpbCZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU="
    html_content=urllib.request.urlopen(url).read()

    soup = bs4.BeautifulSoup(html_content, "html.parser")

    price = soup.find(id="priceblock_ourprice").get_text()
    price= float(price.replace(",","").replace("₹",""))
    price_list.append(price)
    return price

def send_email(msg):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("sender-email","password")
    s.sendmail("sender_email","reciever_email",msg)
    s.quit()

def price_decrease_check(price_list):
    if price_list[-1] < price_list[-2]:
        return True
    else:
        return False

count = 1
while True:
    current_price = check_price()
    if count > 1:
        flag = price_decrease_check(price_list)
        if flag:
            decrease = price_list[-1] - price_list[-2]
            message = f"The price has decrease please check the item. The price decrease by {decrease} rupees."
            send_email(message)
    time.sleep(60000)
    count += 1


