upath=/Users/Mike
wpath=$upath/data/localjobs/mix-getter
datadir=$wpath/mixes
dldir=$datadir/dls
dimg="dijksterhuis/youtube-dl-audio:mixes"

docker build --no-cache -t $dimgdimg $wpath

cp $upath/Desktop/sites/mixes.txt $datadir/urls.txt
docker run -it --rm -v $datadir/:/home/to-get-list/ -v $dldir:/home/gotten/ $dimg /bin/ash -c "echo 'running' ; python /home/get_audio.py"
