FROM node:12.18.2-alpine3.9
WORKDIR /root/coco
COPY my_node.js /root/coco/my_node.js
COPY root /var/spool/cron/crontabs/root
COPY ["package.json", "package-lock.json*", "/root/coco/"]
RUN npm i
RUN chmod +x /root/coco/my_node.js
CMD crond -l 2 -f
