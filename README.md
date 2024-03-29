## Basic project used to report data from a NodeMCU using the DHT22 sensor.

![chart](https://i.ibb.co/F01j7T3/Screenshot-2023-03-10-at-21-47-07.png)
<img align="left" height="350" src="https://pbs.twimg.com/media/Fq7ic9aWcAA9tMP?format=jpg&name=small">


Idea and execution: https://twitter.com/alin__alexandru/status/1633851944501407745

### Env vars
- AUTH_USER - user for basic auth (default to admin)
- AUTH_PASSWORD. -password for basic auth (default to admin)
- CHART_TITLE - title to show on index.html or legend of the chart (default to cigar cabinet)
- MAX_RECORDS - number of records to keep (default to 10)
- SOCKET_URL - app host URL (default to http://127.0.0.1:5000)

Run command: `docker run -p 5000:5000 -e AUTH_USER="admin" -e AUTH_PASSWORD="admin" skykery/temp_humidity_reporter`

### Add entries
GET http://127.0.0.1:5000/add?t=10&h=110

# NodeMcu ESP8266 + DHT22 script
The script I'm using currently on my NodeMcu ESP8266 + DHT22 sensor: https://github.com/skykery/nodemcu-dht22-script
