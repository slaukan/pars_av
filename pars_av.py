import requests
from bs4 import BeautifulSoup


def get_first_car():
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
    }
    url = "https://cars.av.by/filter?seller_type[0]=1&creation_date=10&sort=4"
    r = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(r.text, "lxml")
    
    about_car = soup.find("h3", class_="listing-item__title").text.strip()
    params_car = soup.find("div", class_="listing-item__params").text.strip()
    price_car = soup.find("div", class_="listing-item__prices").text.strip()
    url_car = f'https://cars.av.by{soup.find("a", class_="listing-item__link").get("href")}'

    # print(url_car)
    # n = requests.get(url=url_car, headers=headers)
    # soup1 = BeautifulSoup(n.text, "lxml")
    # print(soup1.find("p", class_="phones__title"))
    # # number = soup1.find("ul", class_="phones__list").find("li").text.strip()
    # print(soup1.find("div", class_ = "phones__card"))
    
    info_car = [about_car,params_car,price_car,url_car]
    return info_car
    

get_first_car()

