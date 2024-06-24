# Dockerfile servidor web Nginx
FROM nginx:mainline-alpine
# Eliminamos los sites pro default de nginx
RUN rm /etc/nginx/conf.d/*
# Añadimos nuestra config
ADD site.conf /etc/nginx/conf.d/
# Añadimos nuestro index x defecto
ADD /site/index.html /usr/share/nginx/html/
# Exponemos puerto
EXPOSE 8080

CMD ["nginx", "-g", "daemon off;"]