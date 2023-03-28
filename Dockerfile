# Pull base image
FROM python:3.9-buster

# Set up directories
RUN apt-get update && apt-get install nginx vim -y --no-install-recommends
COPY nginx.default /etc/nginx/sites-available/default
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
&& ln -sf /dev/stderr /var/log/nginx/error.log

RUN mkdir -p /opt/app
RUN mkdir -p /opt/app/helper_classes
RUN mkdir -p /opt/app/mysite
COPY requirements.txt start-server.sh /opt/app/
COPY mysite /opt/app/mysite/
COPY helper_classes /opt/app/helper_classes/
WORKDIR /opt/app
RUN pip install -r requirements.txt
RUN chown -R www-data:www-data /opt/app

# Install sbom generating tool (syft) into appropriate directory
RUN curl -sSfL https://raw.githubusercontent.com/anchore/syft/main/install.sh | sh -s -- -b /usr/local/bin

# Start server
EXPOSE 8020
STOPSIGNAL SIGTERM
CMD ["/opt/app/start-server.sh"]