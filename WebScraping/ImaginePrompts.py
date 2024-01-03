from operator import length_hint
from bs4 import BeautifulSoup
import re

def process_html_content(html_content):
    pattern = r'prompt: (.*?--v)'
    
    photo_prompts = []
    soup = BeautifulSoup(html_content, 'html.parser')

    og_descriptions = soup.find_all('meta', {'property': 'og:description'})

    for og_description in og_descriptions:
        content_value = og_description.get('content')
        if content_value:
            photo_prompts.append(content_value)

    mah_list = []
    for i in photo_prompts:
        matches = re.findall(pattern, i)
        # Append each modified string to mah_list
        mah_list.extend([s + " 6.0" for s in matches])

    return mah_list

if __name__ == "__main__":
    html_content = """
    <meta property="og:title" content="Midjourney vibe"/>
    <meta property="og:description" content="Flaherty/imagine prompt: Flakey Photo of man in a suit --ar 9:16 --seed 456 --fast --v 5.2/imagine prompt: Parky Picture of blade of grass --ar 9:16 --seed 456 --fast --v"/>
    <meta property="og:image:width" content="216"/>
    <meta property="og:image:height" content="1356"/>
    <meta property="og:image:type" content="image/png"/>
    <meta property="og:type" content="article"/>
    <meta property="og:article:published_time" content="2022-11-02 22:49:59"/>
    <meta property="og:description" content="Deemggen/imagine prompt: Image of Cat on Mat --ar 9:16 --seed 456 --fast --v 5.2/imagine prompt: Funny carpet on staircase --ar 9:16 --seed 456 --fast --v"/>
    <meta property="og:article:modified_time" content="2022-11-05 17:58:35"/>
    """

    result = process_html_content(html_content)

    print(result)
    print(length_hint(result))
