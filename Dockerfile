# Vulnerable Dockerfile Example
FROM ubuntu:14.04

# Install an outdated and vulnerable package
RUN apt-get update && apt-get install -y openssl=1.0.1f-1ubuntu2

# Sample application setup
RUN echo 'Hello, world!' > /var/www/html/index.html
