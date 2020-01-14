# masterypoints-tracker

This is a little script to pull the chamoion mastery point data of League of Legends accounts.  
Currently, this scritpt wraps around the public API of [masterypoints.com](https://masterypoints.com) and the Data Dragon API of Riot Games. This is because in t his way, you don't need to pass an API key for the Riot API and it is currently easier to implement. Maybe later, I will swap out the masterypoints API with the official Riot API endpoints.

## Usage

> When you are using windows, you might use the command `py` instead of `python3`.

### Installation

First of all, you need a python installation of python version 3.6 or newer.

Then, clone the repository and install dependencies using pip:
```
$ git clone https://github.com/zekroTJA/masterypoints-tracker.git
$ python3 -m pip install -r requirements.txt
```

### Specify Output Module

There are different output modules available which are located in `mp-tracker/output`. These are defined following the abstract class `Output` located in `mp-tracker/output/output.py`. Then, you can set the drivers class which should be used in `mp-tracker/const/outputdriver.py`. 

Alternatively, you can also use the output driver injection script `scripts/inject-output-driver.sh`:
```
$ bash ./scripts/inject-output-driver.sh mongo
```

The output module automatically specifies input flags which can then be displayed using the `--help` flag.

### Run Once

Here are some examples how you can run the script.

Running the script using the file output and filtering resuls for chamions Ahri, Kai'Sa, Kindred and Dr. Mundo:
```
$ python3 ./mp-tracker/main.py \
    --username username1 username2 \
    --server euw \
    --loglevel 20 \
    --champions ahri kaisa kindred drmundo \
    --output ./output \
    --indent
```

Or when you are usign the MongoDB output driver:
```
$ python3 ./mp-tracker/main.py \
    --username username1 username2 \
    --server euw \
    --loglevel 20 \
    --champions ahri kaisa kindred drmundo \
    --connection mongodb://user:password@host/authDatabase \
    --database database
```

### Run in Scheduler Mode

Here are some examples how you can run the script in scheduler mode:

Running the script every hour, for example:
```
$ python3 ./mp-tracker/main.py \
    --username username1 username2 \
    --server euw \
    --loglevel 20 \
    --schedule \
    --every 60
```

Or running the script each day at 03.00 for example:
```
$ python3 ./mp-tracker/main.py \
    --username username1 username2 \
    --server euw \
    --loglevel 20 \
    --schedule \
    --daily "03:00"
```

## Docker Image

You can use the provided `Dockerfile` to build this script into a Docker image:
```
$ docker build . -t mp-tracker
```

The image uses the script as entrypoint, which means, you have to pass the command arguments as command to the container at start:
```
$ docker run -d --name mp-tracker mp-tracker \
    -u username1 -s euw --schedule --daily "03:00" \
    -con mongo://uname:pw@host/authdb -db masterypoints
```

Or, if you are using docker-compose:
```yml
mp-tracker:
  image: 'mp-tracker'
  command: '-u username1 -s euw --schedule --daily "03:00" -con mongo://uname:pw@host/authdb -db masterypoints'
  restart: 'on-failure'
```

---

© 2020 Ringo Hoffmann (zekro Development)  
Covered by the MIT Licence.