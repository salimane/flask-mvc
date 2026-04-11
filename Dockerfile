FROM python:3.14-alpine

LABEL maintainer="me@salimane.com" \
      vendor="salimane" \
      name="salimane/flask-mvc" \
      description="Python boilerplate application following MVC pattern using Flask." \
      com.salimane.component.name="flask-mvc" \
      com.salimane.component.distribution-scope="public" \
      com.salimane.component.changelog-url="https://github.com/salimane/flask-mvc/releases" \
      com.salimane.component.url="https://github.com/salimane/flask-mvc"

ARG BUILD_DATE
ARG VCS_REF
ARG VCS_REF_MSG
ARG VCS_URL
ARG VERSION

LABEL com.salimane.component.build-date="$BUILD_DATE" \
      com.salimane.component.vcs-url="$VCS_URL" \
      com.salimane.component.vcs-ref="$VCS_REF" \
      com.salimane.component.vcs-ref-msg="$VCS_REF_MSG" \
      com.salimane.component.version="$VERSION"

ENV LANG=en_US.UTF-8 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN apk --no-cache add gcc musl-dev libffi-dev openssl-dev \
        postgresql-dev libpq && \
    rm -rf /var/cache/apk/*

WORKDIR /opt/flask

# Install dependencies first (cached layer unless requirements.txt changes)
COPY requirements.txt .
RUN pip install --no-cache-dir -U pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy application source
COPY . .

EXPOSE 16000

CMD ["gunicorn", "runserver:app", "--bind", "0.0.0.0:16000", "--workers", "4", "--threads", "2", "--worker-class", "sync"]
