# Vulnerable Dockerfile Example
FROM httpd:2.4.29

# Copy some website content (example)
COPY . /usr/local/apache2/htdocs/

