#!/bin/bash
C=$(docker run -it -d -p 5000:5000 csirtgadgets/csirtg-predictd)

echo "Getting a shell into the container..."
docker exec -it $C /bin/bash