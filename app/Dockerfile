# Build
FROM python:3.9.1-slim-buster as build

ENV \
  DEBIAN_FRONTEND=noninteractive \
  PATH=$PATH:/app/bin/ \
  PYTHONUSERBASE=/app

COPY main.py /app/main.py
COPY requirements.txt /tmp/requirements.txt

RUN set -x \
  && mkdir -p "$PYTHONUSERBASE" \
  && pip install \
    --prefix="${PYTHONUSERBASE}" \
    -r /tmp/requirements.txt \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

# Run
FROM python:3.9.1-slim-buster

ENV \
  APP_VERSION=v1.0.0 \
  FLASK_APP=/app/main.py \
  PYTHONUSERBASE=/app \
  PATH=$PATH:/app/bin/

COPY --from=build "$PYTHONUSERBASE" "$PYTHONUSERBASE"

USER nobody:nogroup

EXPOSE 5000/tcp

CMD ["flask", "run"]
