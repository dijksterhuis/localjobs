#!/usr/bin/env python

from __future__ import unicode_literals
import youtube_dl, os

class MyLogger(object):
    def debug(self, msg):
        print('Debugger: ',msg)
    def warning(self, msg):
        print('Warning: ',msg)
    def error(self, msg):
        print('Error: ',msg)

def my_hook(d):
    if d['status'] == 'finished':
        print('Converting: ' + d['filename'])
    if d['status'] == 'downloading':
        print('Downloading: ' + d['filename'])

def main():
    os.chdir('/home/gotten/')
    ydl_opts = {
        'format': 'bestaudio/best', \
        'postprocessors': [{'key': 'FFmpegExtractAudio','preferredcodec': 'wav'}], \
        'logger': MyLogger(), \
        'progress_hooks': [my_hook], \
    }

    data_dict = { 'urls' : [] }
    with open('/home/to-get-list/urls.txt','r') as f:
        lines = f.readlines()
        data_dict['dls'] = [ i.rstrip('\r\n') if len(lines) > 1 else lines for i in lines ]
    for url in data_dict['dls']:
        with open('/home/to-get-list/old_urls.txt','r+') as ch_f:
            data_dict['checks'] = [ line.rstrip('\n\r') for line in ch_f.readlines() ]
        if url in data_dict['checks']:
            print('url previously downloaded: ' + url)
            pass
        else:
            data_dict['urls'].append(url)
            with open('/home/to-get-list/old_urls.txt','a+') as out_f:
                out_f.write( url + '\n' )

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download( data_dict['urls'] )

if __name__ == '__main__':
    main()
