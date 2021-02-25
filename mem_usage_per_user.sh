#!/bin/bash

if [[ "$1" = "-h" || "$1" = "--help" ]]
then
        echo "Usage: $(basename $0) [user]"
        echo ""
        echo "  -h [--help] - shows this help"
        exit 0
fi

if [[ -z $1 ]]
then
        for i in `ps -e -o user --no-header | sort | uniq`; do
                echo "$i: $(ps -u $i  -o rss --no-header | paste -sd+ -| bc)KB"
        done;
else
        echo "$1: $(ps -u $1  -o rss --no-header | paste -sd+ -| bc) KB"
fi
