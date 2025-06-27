# ──────────────────────────────────────────────────────────────
# Base image – Ubuntu 18.04 (stable for OpenBTS tooling)
# ──────────────────────────────────────────────────────────────
FROM ubuntu:18.04

LABEL maintainer="charis.rhea@gmail.com"
ENV DEBIAN_FRONTEND=noninteractive

# ───────────── 1. Core packages ─────────────
RUN apt-get update && apt-get install -y \
    build-essential curl git wget unzip \
    python3 python3-pip python3-dev python3-setuptools \
    sqlite3 net-tools iputils-ping dnsutils \
    ca-certificates sudo gnupg2 \
    # optional – comment out if you don’t need GUI Wireshark inside the container
    tshark                       \
 && apt-get clean && rm -rf /var/lib/apt/lists/*

# ───────────── 2. Upgrade CMake (needed only if you compile OpenBTS) ─────────────
RUN wget -q https://github.com/Kitware/CMake/releases/download/v3.16.9/cmake-3.16.9-Linux-x86_64.sh \
 && chmod +x cmake-3.16.9-Linux-x86_64.sh \
 && ./cmake-3.16.9-Linux-x86_64.sh --skip-license --prefix=/usr/local \
 && rm cmake-3.16.9-Linux-x86_64.sh

# ───────────── 3. Clone *simulation-only* OpenBTS repo ─────────────
# NOTE:  we only need the scripts/configs – we’re **not** building UHD/HackRF here.
WORKDIR /root
RUN git clone https://github.com/CorteXlab/openbts-docker.git

# ───────────── 4. Copy your detection code ─────────────
# The build context will be the project root (where docker-compose.yml lives)
WORKDIR /root/detector
COPY detection/ ./          
RUN pip3 install pandas

# ───────────── 5. Default entrypoint ─────────────
#   Log directory `/root/detector/logs` will be mounted from the host
CMD ["python3", "detect_bts.py"]
