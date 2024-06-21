# Dockerfile para el servidor web (Nginx) con soporte SSL
FROM nginx:latest

# Copiar la configuración personalizada de Nginx
COPY nginx.conf /etc/nginx/nginx.conf

# Copiar los certificados SSL (reemplaza los path/to con tus propios certificados)
COPY certs/server.crt /etc/ssl/certs/
COPY certs/server.key /etc/ssl/private/

# Copiar los archivos del sitio web
COPY site /usr/share/nginx/html

# Exponer los puertos 80 y 443
EXPOSE 80
EXPOSE 443

CMD ["nginx", "-g", "daemon off;"]
