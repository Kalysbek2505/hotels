import csv

import bs4
import logging

import requests

# logging.basicConfig(level=logging.DEBUG)
# logger = logging.getLogger('wb')


HEADERS = ['Price', 'Name', 'Unicode', 'href']
# data = []

class Client:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers = {
            'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36', 
            'Accept-Language': 'ru',
        }
        self.result = []
        self.init_csv()
    
    def save_to_res(self, *args):
        # print(args)
        # for idx, item in enumerate(args):
        #     print(idx, type(item), item)

        # if isinstance(item, bs4.BeautifulSoup):
        #     self.result.append(item.text.strip())
        # else:
        #     self.result.append(item)

        
        # self.result.append(
        #     [item.text.strip() if isinstance(item, bs4.BeautifulSoup) else item for item in args]
        # )
        # print('saving_to_res')
        # for item in args:
        #     print(type(item))
        #     print(isinstance(item, bs4.BeautifulSoup))

        self.save_results([item.text.strip() if isinstance(item, bs4.element.Tag) else item for item in args])

    def parser_pages(self):
        for page in range(1,5): 
            url = f'https://www.qifa.ru/catalog/odegda/shkolniy_bazar_odegda_rf?page={page}'
            r = requests.get(url)
            soup = bs4.BeautifulSoup(r.text, 'lxml')
            items = soup.find('div', class_='grid__item').find_all('div', class_='grid-view-item')

            for item in items:
                href = 'https://www.qifa.ru' + item.find('a', class_ = 'grid-view-item__link').get('href')
                price = item.find('span', class_='price')
                names = item.find('p', class_='h4 grid-view-item__title list_first_tit')
                spu_ = item.find('div', class_='spu')
                
                # print(href)
                # print(spu_.text.strip())
                # print(names.text)
                # print(price.text)
                self.save_to_res(price, names, spu_, href)
                # data.append([
                #     price.text.strip(), 
                #     names.text.strip(), 
                #     spu_.text.strip(),
                #     href.text.strip()
                # ])
                # print(data)
    def obuv_parser(self):
        for page in range(1,33):
            url = f'https://www.qifa.ru/catalog/obuv/shkolniy_bazar_obuv_rf?page={page}'
            r = requests.get(url)
            soup = bs4.BeautifulSoup(r.text, 'lxml')
            items = soup.find('div', class_='grid__item').find_all('div', class_='grid-view-item')

            for item in items:
                
                href = 'https://www.qifa.ru' + item.find('a', class_ = 'grid-view-item__link').get('href')
                price = item.find('span', class_='price')
                names = item.find('p', class_='h4 grid-view-item__title list_first_tit')
                spu_ = item.find('div', class_='spu')
                
                # print(spu_.text)
                # print(names.text)
                # print(price.text)
                # data.append([price.text, names.text, spu_.text])
                self.save_to_res(price, names, spu_, href)
                # data.append([
                #     price.text.strip(), 
                #     names.text.strip(), 
                #     spu_.text.strip(),
                #     href.text.strip()
                # ])
                # print(data)
    def sumka_parser(self):
        for page in range(1,5):
            url = f'https://www.qifa.ru/catalog/sumki/shkolniy_bazar_sumki_i_ryukzaki_rf?page={page}'
            r = requests.get(url)
            soup = bs4.BeautifulSoup(r.text, 'lxml')
            items = soup.find('div', class_='grid__item').find_all('div', class_='grid-view-item')

            for item in items:
                # imges = item.find('img', class_='grid-view-item__image  primary').get('src')
                href = 'https://www.qifa.ru' + item.find('a', class_ = 'grid-view-item__link').get('href')

                price = item.find('span', class_='price')
                names = item.find('p', class_='h4 grid-view-item__title list_first_tit')
                spu_ = item.find('div', class_='spu')

                # print(href.text)
                # print(spu_.text)
                # print(names.text)
                # print(price.text)
                # data.append([price.text, names.text, spu_.text])
                self.save_to_res(price, names, spu_, href)
                # data.append([
                #     price.text.strip(), 
                #     names.text.strip(), 
                #     spu_.text.strip(),
                #     href.text.strip(),
                #     imges.text.strip()
                # ])
                # print(data)

    def noski_parser(self):
        for page in range(1,4):
            url = f'https://www.qifa.ru/catalog/noski_i_chulki/shkolniy_baza_noski_i_kolgotki_rf?page={page}'
            r = requests.get(url)
            soup = bs4.BeautifulSoup(r.text, 'lxml')
            items = soup.find('div', class_='grid__item').find_all('div', class_='grid-view-item')

            for item in items:
                
                href = 'https://www.qifa.ru' + item.find('a', class_ = 'grid-view-item__link').get('href')
                price = item.find('span', class_='price')
                names = item.find('p', class_='h4 grid-view-item__title list_first_tit')
                spu_ = item.find('div', class_='spu')
                
                # print(spu_.text)
                # print(names.text)
                # print(price.text)
                # data.append([price.text, names.text, spu_.text])
                self.save_to_res(price, names, spu_, href)
                # data.append([
                #     price.text.strip(), 
                #     names.text.strip(), 
                #     spu_.text.strip(),
                #     href.text.strip()
                # ])
                # print(data)
    def texnika_parser(self):
        url = f'https://www.qifa.ru/catalog/bitovaya_tehnika_i_elektronika/postavka_iz_rf_umnaya_tehnika'
        r = requests.get(url)
        soup = bs4.BeautifulSoup(r.text, 'lxml')
        items = soup.find('div', class_='grid__item').find_all('div', class_='grid-view-item')

        for item in items:
            href = 'https://www.qifa.ru' + item.find('a', class_ = 'grid-view-item__link').get('href')    
            price = item.find('span', class_='price')
            names = item.find('p', class_='h4 grid-view-item__title list_first_tit')
            spu_ = item.find('div', class_='spu')
                
            # self.save_to_res(price, names, spu_, href)
            # print(spu_.text)
            # print(names.text)
            # print(price.text)
            # data.append([price.text, names.text, spu_.text])
            self.save_to_res(price, names, spu_, href)
            # data.append([
            #     price.text.strip(), 
            #     names.text.strip(), 
            #     spu_.text.strip(),
            #     href.text.strip()
            # ])
            # print(data)
    def init_csv(self):
        path = 'test.csv'
        with open(path, 'w') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(HEADERS)

    def save_results(self, data):
        path = 'test.csv'
        with open(path, 'a') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(data)
        
        # import csv
        # path = 'test.csv'
        # # open(path, 'w').close()
        # with open(path, 'a') as csv_file:
        #     writer = csv.writer(csv_file)
        #     writer.writerow(HEADERS)
        #     for data in self.result:
        #         writer.writerow(data)
        # df = pd.DataFrame(data, columns=HEADERS)
        # df = pd.DataFrame(self.result, columns=HEADERS)
        # df.to_csv('res.csv', sep=';', encoding='utf8')

        
            

    # def load_page(self):
    #     for i in range(1,4):

    #         url = f'https://www.qifa.ru/catalog/odegda/shkolniy_bazar_odegda_rf?page={i}'
    #         res = self.session.get(url = url)
    #         res.raise_for_status()
    #         return res.text
    
    # def parse_page(self, text: str):
    #     soup = bs4.BeautifulSoup(text, 'lxml')
    #     items = soup.find('div', class_='grid__item').find_all('div', class_='grid-view-item')

    #     for item in items:
    #         price = item.find('span', class_='price')
    #         names = item.find('p', class_='h4 grid-view-item__title list_first_tit')
    #         spu_ = item.find('div', class_='spu')
    #         print(spu_.text)
    #         print(names.text)
    #         print(price.text)


        # container = soup.select('div.item__link_div')
        # print(items)
        # for block in container:
        #     self.parse_block(block=block)

    # def parse_block(self, block):
    #     # logger.info(block)
    #     # logger.info('=' * 100)
    #     url_block = block.select_one('a.grid-view-item__link')
    #     if not url_block:
    #         logger.error('no url_block')
    #         return
    #     url = url_block.get('href')
    #     if not url:
    #         logger.error('no href')
    #         return

    #     name_block = block.select_one('span.price')
    #     if not name_block:
    #         logger.error(f'no name_block on {url}')
    #         return

    #     name_block = name_block.text
    #     name_block = name_block.replace('/', '').strip()

        


    #     logger.info('%s', f'https://www.qifa.ru{url}')

    def run(self):
        text = self.parser_pages()
        text1 = self.obuv_parser()
        text3 = self.sumka_parser()
        text4 = self.noski_parser()
        text5 = self.texnika_parser()
        # self.save_results()

if __name__ == '__main__':
    parser = Client()
    parser.run()
    