FROM python:alpine
LABEL author="michael robeson (Dijksterhuis)" \
      project="youtube-audio-downloader" \
      name="youtube-dl" \
      purpose="Download youtube audio data" \
      version=“1”

RUN apk update ; apk upgrade ; apk add curl ffmpeg

# youtube-dl stuff

RUN pip install --upgrade youtube-dl

# you can map to-get-list to the directory holding the .txt file to get a list of files TODO!
# or you can run the docker image only mapping the gotten folder, which is where files will downlaod to

COPY get_audio.py /home/
RUN mkdir /home/to-get-list
RUN mkdir /home/gotten

ENTRYPOINT ["/bin/ash"]
COMMAND ["/home/get_audio.py"]
