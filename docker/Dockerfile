FROM python:3.9-slim-bullseye

ARG APP_USER=django

RUN apt-get update && apt-get install --yes --no-install-recommends bash=5.1-2+deb11u1 xmlsec1=1.2.31-1 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && useradd -m -U -u 1000 -s /bin/sh ${APP_USER}

COPY docker/docker-entrypoint.sh /bin/
WORKDIR /home/${APP_USER}

COPY ./requirements.txt .

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt \
    && chmod +x /bin/docker-entrypoint.sh

COPY --chown=${APP_USER} --chmod=755 . .

EXPOSE 8000

USER ${APP_USER}

ENTRYPOINT [ "/bin/docker-entrypoint.sh" ]