# Dockerfile para usar Ubuntu con servidor web Nginx
FROM nginx:mainline-alpine

RUN rm /etc/nginx/conf.d/*

ADD site.conf /etc/nginx/conf.d/

ADD /site/index.html /usr/share/nginx/html/

EXPOSE 82

CMD ["nginx", "-g", "daemon off;"]
