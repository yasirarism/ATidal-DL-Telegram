# Docker Ubuntu Kinetic
FROM yasirarism/indocloud-docker:kinetic

COPY . .
CMD ["bash","start.sh"]