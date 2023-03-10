Basic project used to report data from an NodeMCU using the DHT22 sensor.
![status page](https://i.ibb.co/TrqQpK9/chart.gif)

### Env vars
- AUTH_USER - user for basic auth (default to admin)
- AUTH_PASSWORD. -password for basic auth (default to admin)
- CHART_TITLE - title to show on index.html or legend of the chart (default to cigar cabinet)
- MAX_RECORDS - number of records to keep (default to 10)
- SOCKET_URL - app host URL (default to http://127.0.0.1:5000)

Run command: `docker run -p 5000:5000 -e AUTH_USER="admin" -e AUTH_PASSWORD="admin" skykery/temp_humidity_reporter`

### Add entries
GET http://127.0.0.1:5000/add?t=10&h=110
