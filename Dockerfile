FROM python:3.8-slim-buster
LABEL maintainer="zekro <contact@zekro.de>"
ARG OUTPUT_DRIVER="mongo"
ENV RUNARGS=""

WORKDIR /app
ADD . .
RUN bash ./scripts/inject-output-driver.sh \
        $OUTPUT_DRIVER \
        ./mp-tracker/const/outputdriver.py

RUN python3 -m pip install -r ./requirements.txt

ENTRYPOINT ["python3", "./mp-tracker/main.py", "-l20"]