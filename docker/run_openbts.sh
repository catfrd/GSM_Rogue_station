#!/bin/bash

# Set the image name
IMAGE_NAME="roguebts-sim"

echo "🔧 Step 1: Building Docker image..."
docker build -t $IMAGE_NAME .

# Ensure the host logs directory exists
mkdir -p ../logs

echo "🚀 Step 2: Running simulation container..."
docker run --rm -it \
  -v "$(pwd)/../logs:/root/detector/logs" \
  --name roguebts_container \
  $IMAGE_NAME
