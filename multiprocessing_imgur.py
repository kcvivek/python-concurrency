####
# This sample is published as part of the blog article at www.toptal.com/blog 
# Visit www.toptal.com/blog and subscribe to our newsletter to read great posts
####

from functools import partial
import logging
from multiprocessing.pool import Pool
import os
from time import time

from download import setup_download_dir, get_links, download_link


logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger('requests').setLevel(logging.CRITICAL)
logger = logging.getLogger(__name__)


def main():
    ts = time()
    client_id = os.getenv('IMGUR_CLIENT_ID')
    if not client_id:
        raise Exception("Couldn't find IMGUR_CLIENT_ID environment variable!")
    download_dir = setup_download_dir()
    links = [l for l in get_links(client_id) if l.endswith('.jpg')]
    download = partial(download_link, download_dir)
    with Pool(8) as p:
        p.map(download, links)
    print('Took {}s'.format(time() - ts))


if __name__ == '__main__':
    main()

