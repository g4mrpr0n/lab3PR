import requests
import json
from bs4 import BeautifulSoup

url = "https://999.md/ro/76325396"

def scrapper(url):

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        features_div = soup.find('div', class_='adPage__content__features')

        data_dict = {}

        h2_elements = features_div.find_all('h2')

        for h2 in h2_elements:
            category_name = h2.text.strip()
            ul_element = h2.find_next('ul')
            
            if ul_element:
                feature_data = {}
                
                li_elements = ul_element.find_all('li')
                
                for li in li_elements:
                    key_element = li.find('span', class_='adPage__content__features__key')
                    value_element = li.find('span', class_='adPage__content__features__value')
                    
                    if key_element:
                        key = key_element.text.strip()
                        
                        if 'm-value' in li['class']:
                            if value_element:
                                value = value_element.text.strip()
                                feature_data[key] = value
                        else:
                            values = [item.text.strip() for item in li.find_all('span', class_='m-no_value')]
                            feature_data[key] = values
                
                data_dict[category_name] = feature_data
        
        result_json = json.dumps(data_dict, ensure_ascii=False, indent=4)
        
        print(result_json)

    else:
        print('Failed to retrieve the web page. Status code:', response.status_code)


def main():
    scrapper(url)

if __name__ == "__main__":
   main()