#!/usr/bin/env bash

#set -x

usage () {
    echo "Script to download youtube playlists as mp3"
    echo "Usage:"
    echo -e "\t $(basename $0) playlistId [dest_folder]"
    echo "Where:"
    echo -e "\t playlistsId - youtube playlist for download, you can find it in browser"
    echo -e "\t dest_folder - where to store downloaded files. If not provided will be used current folder"
    exit 0
}

YOUTUBE_DL=/usr/bin/youtube-dl
FOR_RENAME='NA-NA _-_ NA-_ _-NA'
[[ -z $1 ]] && usage || PLID=$1
[[ -z $2 ]] && DEST=$(dirname $0) || DEST=$2

mkdir -p $DEST && cd $DEST
echo "$(date -u) Start downloading"
$YOUTUBE_DL --extract-audio -4 --audio-format "mp3" --retries 3 --audio-quality 0 -o "%(artist)s-%(track)s-%(id)s.%(ext)s" --prefer-ffmpeg --restrict-filenames --continue --no-progress --ignore-errors --embed-thumbnail --download-archive $DEST/download-archive.txt --sleep-interval 5 "https://www.youtube.com/playlist?list=$PLID"
echo "$(date -u) Download completed"

#Not all video has artist and track metadata
echo "$(date -u) Rename files"
for id in $(cut -d" " -f2 download-archive.txt); do
    if ls *${id}.mp3 &>/dev/null; then
        file=$(ls *${id}.mp3)
        name=${file::-16}
        if [[ $FOR_RENAME = *${name}* ]]; then
            name=$($YOUTUBE_DL --retries 3 --ignore-errors --restrict-filenames -o "%(title)s" --get-filename "https://www.youtube.com/watch?v=$id")
        fi
    mv --backup --suffix=.bak $file ${name}.mp3
    fi
done    
echo "$(date -u) Rename completed"
