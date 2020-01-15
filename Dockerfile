FROM python:3.8-slim-buster
LABEL maintainer="zekro <contact@zekro.de>"
ARG DATA_DRIVER="mongo"

WORKDIR /app
ADD . .
RUN bash ./scripts/inject-driver.sh \
        $DATA_DRIVER \
        ./mp-tracker/const/datadriver.py

RUN python3 -m pip install -r ./requirements.txt

ENTRYPOINT ["python3", "./mp-tracker/main.py", "-l20"]