#!/usr/local/bin/python3.6

import os
from requests import get

def get_urls(in_path):
    filenames = [ filename for filename in os.listdir(in_path) if '.txt' in filename ]
    to_get_list = list()
    for filename in filenames:
        with open(in_path + filename,'r') as f:
            urls = [ i.rstrip('\r\n') for i in f.readlines() if '.pdf' in i[-10:] ]
        if len(urls) == 0: pass
        else:
            for url in urls:
                to_get_list.append(url)
    return to_get_list

def get_pdfs(urls,out_path):
    for url in urls:
        out_name = url.split('/')[-1:][0]
        if out_name in os.listdir(out_path): pass
        else:
            print('Saving: ' + url + ' as: ' + out_name )
            pdf = get(url)
            with open( out_path + out_name , 'wb') as f:
                f.write(pdf.content)

def main():
    in_path = '/Users/Mike/Desktop/sites/'
    out_path = '/Users/Mike/data/localjobs/paper-getter/pdfs/'
    get_pdfs( get_urls( in_path ) , out_path )

if __name__ == '__main__':
    main()
