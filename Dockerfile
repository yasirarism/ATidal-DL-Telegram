# Docker Ubuntu Kinetic
FROM yasirarism/indocloud-docker:kinetic

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt
COPY . .
CMD ["bash","start.sh"]