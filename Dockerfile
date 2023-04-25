FROM python:3.10-alpine
MAINTAINER me@salimane.com

# Set locale to UTF-8
ENV LANG en_US.UTF-8

RUN apk --no-cache add g++ gcc git jpeg-dev libffi-dev libjpeg libxml2-dev \
    libxslt-dev linux-headers musl-dev openldap-dev openssl postgresql-dev zlib zlib-dev && \
    rm -rf /var/cache/apk/*

ENV LIBRARY_PATH=/lib:/usr/lib
WORKDIR /opt/flask
RUN pip install -U pip setuptools
RUN pip install -r /opt/flask/requirements.txt
RUN pip install uwsgi

EXPOSE 16000
CMD ["sh", "-c", "sleep 5 ; uwsgi --http 0.0.0.0:16000 --wsgi-file runserver.py --callable app --processes 8 --threads 2"]

ARG BUILD_DATE
ARG VCS_REF
ARG VCS_REF_MSG
ARG VCS_URL
ARG VERSION

LABEL vendor="salimane" \
      name="salimane/flask-mvc" \
      maintainer="me@salimane.com" \
      description="python boilerplate application following MVC pattern using flask micro framework." \
      com.salimane.component.name="flask-mvc" \
      com.salimane.component.build-date="$BUILD_DATE" \
      com.salimane.component.vcs-url="$VCS_URL" \
      com.salimane.component.vcs-ref="$VCS_REF" \
      com.salimane.component.vcs-ref-msg="$VCS_REF_MSG" \
      com.salimane.component.version="$VERSION" \
      com.salimane.component.distribution-scope="public" \
      com.salimane.component.changelog-url="https://github.com/salimane/flask-mvc/releases" \
      com.salimane.component.url="https://github.com/salimane/flask-mvc" \
      com.salimane.component.run="docker run -e ENV_NAME=ENV_VALUE -p 16000:16000/tcp IMAGE" \
      com.salimane.component.environment.required="" \
      com.salimane.component.environment.optional="" \
      com.salimane.component.dockerfile="/usr/src/app/Dockerfile"
