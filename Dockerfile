FROM python:3.8-slim-buster
LABEL maintainer="zekro <contact@zekro.de>"
ARG OUTPUT_DRIVER="mongo"
ENV RUNARGS=""

WORKDIR /app
ADD . .
RUN bash ./scripts/inject-output-driver.sh \
        $OUTPUT_DRIVER \
        ./mp-tracker/const/outputdriver.py

RUN python3 -m pip install -r ./requirements.py

RUN echo "0 6 * * * python3 /app/mp-tracker/main.py \$RUNARGS >> /var/log/cron.log 2>&1" \
        >> /etc/cron.d/mp-tracker
RUN chmod 0644 /etc/cron.d/mp-tracker &&\
    touch /var/log/cron.log
RUN apt-get update &&\
    apt-get -y install cron

CMD cron && tail -f /var/log/cron.log