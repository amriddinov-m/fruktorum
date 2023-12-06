import requests
from bs4 import BeautifulSoup


def load_data_from_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        og_title = soup.find('meta', property='og:title')
        og_description = soup.find('meta', property='og:description')
        og_image = soup.find('meta', property='og:image')

        if not og_title:
            title = soup.title.string.strip() if soup.title else None
        else:
            title = og_title['content']

        description = og_description['content'].strip() if og_description else None
        image_url = og_image['content'].strip() if og_image else None
        return {
            'title': title,
            'description': description,
            'image_url': image_url,
        }
    except Exception as e:
        print(f"Ошибка извлечения информации из URL: {e}")
        return None
