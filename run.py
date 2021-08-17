from scrap_inst import Inst


def run(parse_url):
    url = 'https://www.instagram.com/'
    parser = Inst(url, 'uni_temir', 'banan1234')
    parser.auth_inst()
    parser.scrap_followers(parse_url)






















run('https://www.instagram.com/alma.iceee/')