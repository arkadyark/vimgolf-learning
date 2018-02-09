import requests
from bs4 import BeautifulSoup

BASE_URL = "http://vimgolf.com"

def get_links(vimgolf_root_url):
    page_soup = BeautifulSoup(requests.get(vimgolf_root_url).content, 'html.parser')
    return [BASE_URL + challenge.findChild('a').attrs['href'] for challenge in page_soup.select('.challenge')]

def get_challenge(vimgolf_challenge_url):
    data = requests.get(vimgolf_challenge_url).json()
    return data['in']['data'], data['out']['data']

if __name__ == '__main__':
    challenge_links = get_links(BASE_URL)
    for challenge in challenge_links:
        challenge_id = challenge.split('/')[-1]
        infile, outfile = get_challenge(challenge)
        with open('infiles/{}.txt'.format(challenge_id), 'w+') as f:
            f.write(infile)
        with open('outfiles/{}.txt'.format(challenge_id), 'w+') as f:
            f.write(outfile)
