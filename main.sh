#! /bin/sh

python3 src/main.py
cd public && echo "Starting server at http://localhost:8888"&& python3 -m http.server 8888


