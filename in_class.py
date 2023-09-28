import requests
from bs4 import BeautifulSoup

url = "https://999.md/ro/list/phone-and-communication/mobile-phones"
main_link = "https://999.md"

def scrape_page(url_link,url_list=[],max_page_num=None,page_number=1):

    try:
        if page_number <= max_page_num:
            response = requests.get(url_link)
            if response.status_code == 200:
        
                soup = BeautifulSoup(response.text, 'html.parser')

                mydivs = soup.find_all("div", {"class": "ads-list-photo-item-title"})

                for div in mydivs:
                    a_tags = div.find_all('a', href=True) 
                    for a in a_tags:
                        link = a['href']  
                        if main_link+ link not in url_list and link[1]!='b':
                            url_list.append(main_link+link)
                

                next_page = soup.find('li', class_='current').find_next_sibling('li')
                page_next = (str("https://999.md") + next_page.find('a').get('href'))
                scrape_page(page_next, url_list, max_page_num, page_number + 1)
        return url_list

    except requests.exceptions.RequestException as e:
        print(f"An error occurred during the request: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def main():
    url_list=scrape_page(url,url_list=[], max_page_num=5, page_number=1)
    print(url_list)
    with open('links.txt', 'a') as f:
        for everyurl in url_list:
            f.write(everyurl + '\n')

if __name__ == "__main__":
   main()