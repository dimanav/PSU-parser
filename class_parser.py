import requests
from bs4 import BeautifulSoup
undergraduate = 'undergraduate'
graduate = 'graduate'


class Parser:

    def __init__(self, url, education_level):
        self.url = url
        self.education_level = education_level

    def parsing_page(self):
        data_list = []

        response = requests.get(self.url, self.education_level)
        soup = BeautifulSoup(response.text, 'html.parser')

        pagination = soup.find('div', class_='pages_container').find_all('span')
        pages = pagination[-2].text

        for page in range(1, int(pages)+1):

            response = requests.get(self.url+str(page))
            soup = BeautifulSoup(response.text, 'html.parser')

            rows = soup.find('table', class_='list_table').find('tbody').find_all('tr')

            for row in rows:
                columns = row.find_all('td')
                if self.education_level == graduate:
                    if columns[3].text == 'о':
                        data_list.insert(int(columns[0].text)-1, [columns[1].text, columns[4].text])
                if self.education_level == undergraduate:
                    if columns[4].text == 'о':
                        data_list.insert(int(columns[0].text)-1, [columns[1].text, columns[6].text])

        return data_list
