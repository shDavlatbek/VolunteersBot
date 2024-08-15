# Pull official base image
FROM python:3.11.9

# Set work directory
WORKDIR /usr/src/app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV CRYPTOGRAPHY_DONT_BUILD_RUST=1

# Install pip and project dependencies
COPY ./requirements.txt requirements.txt
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Create directory for the app user and set ownership
RUN addgroup --system app && adduser --system --group app \
    && mkdir -p /home/app/web \
    && mkdir /home/app/web/static \
    && mkdir /home/app/web/media \
    && chown -R app:app /home/app/web

# Set the appropriate directories and switch to the app user
ENV HOME=/home/app
ENV APP_HOME=/home/app/web
WORKDIR $APP_HOME

# Copy project files and entrypoint script
COPY . $APP_HOME
COPY ./entrypoint.sh $APP_HOME

# Ensure entrypoint script is executable
RUN chmod +x /home/app/web/entrypoint.sh

# Switch to non-root user
USER app

# Run entrypoint script
ENTRYPOINT ["/home/app/web/entrypoint.sh"]
