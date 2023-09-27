# Use an official Apache image as the base image
FROM httpd:2.4

# Copy a custom HTML file to the document root
COPY index.html /usr/local/apache2/htdocs/index.html

# Update Apache configuration to listen on port 80
RUN echo "Listen 80" >> /usr/local/apache2/conf/httpd.conf
