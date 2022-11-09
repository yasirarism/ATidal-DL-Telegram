# Base Docker
FROM ubuntu:22.10

# Setup Working Directory
WORKDIR /TidalDL
RUN chmod 777 /TidalDL

# Installing basic packages
RUN apt-get update -y && apt install python3-pip apt-utils libpq-dev python-dev -y

# Install Requirements
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .
# Set CMD Bot
CMD ["python3", "-m", "bot"]
