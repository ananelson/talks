set -e
docker build -t dexy/bidsdemo .
docker run -t -i \
    -v `pwd`:/home/repro/work \
    dexy/bidsdemo /bin/bash
