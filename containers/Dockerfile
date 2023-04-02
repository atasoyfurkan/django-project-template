FROM python:3.10-alpine3.16 as builder

RUN apk add --no-cache --no-cache \
    git gcc musl-dev libjpeg-turbo-dev zlib-dev \
    libffi-dev libressl-dev postgresql-dev

WORKDIR /usr/src/app
COPY Pipfile Pipfile.lock ./

RUN	pip3 install --no-cache-dir --upgrade pip pipenv && \
    pipenv requirements --dev > requirements.txt && \
    pip3 wheel \
    --no-cache-dir \
    --wheel-dir wheels \
    -r requirements.txt

FROM python:3.10-alpine3.16

WORKDIR /usr/src/app

COPY --from=builder /usr/src/app/wheels /wheels

RUN addgroup -S app && adduser -u 1000 -S app -G app && \
    apk add --no-cache libpq zlib libjpeg-turbo curl libressl bash && \
    pip3 install --no-cache-dir --upgrade pip pipenv && \
    pip install --no-cache /wheels/*

RUN chown -R app:app /usr/local/lib/python3.10
COPY --chown=app:app . /usr/src/app/

USER app
EXPOSE 8000

# The default command is only used for local development
ENTRYPOINT ["/usr/src/app/containers/entrypoint.sh"]
CMD ["python3 manage.py runserver 0.0.0.0:8000"]
