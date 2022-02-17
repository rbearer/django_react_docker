# Pull the default python image that we can build off of
FROM python:3.11.0a5-alpine3.15

# Set work directory
WORKDIR /usr/src/music_buddy

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# Copy project from volume into container
COPY . .

##########################
# Install Dependencies
##########################

# Install NodeJS
RUN apk add --update nodejs npm

# Update Python Package Manager
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Run entrypoint.sh script
RUN ["chmod", "+x", "/usr/src/music_buddy/entrypoint.sh"]
ENTRYPOINT ["sh", "/usr/src/music_buddy/entrypoint.sh"]

