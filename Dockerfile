FROM python:3.10.3-alpine as builder

# set work directory
WORKDIR /usr/src/Cinema

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev
# lint
RUN pip install --upgrade pip
RUN pip install flake8
COPY . .

# install dependencies
COPY requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/Cinema/wheels -r requirements.txt

#########
# FINAL #
#########

# pull official base image
FROM python:3.10.3-alpine

# create directory for the app user
RUN mkdir -p /home/Cinema

# create the app user
RUN addgroup -S Cinema && adduser -S Cinema -G Cinema


# create the appropriate directories
ENV HOME=/home/Cinema
ENV APP_HOME=/home/Cinema/web
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/mediafiles
WORKDIR $APP_HOME
# install dependencies
RUN apk update && apk add libpq
COPY --from=builder /usr/src/Cinema/wheels /wheels
COPY --from=builder /usr/src/Cinema/requirements.txt .
RUN pip install --no-cache /wheels/*

# copy project
COPY . $APP_HOME
# chown all the files to the app user
RUN chown -R Cinema:Cinema $APP_HOME
# change to the app user
USER Cinema

