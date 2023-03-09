Basic project used to report data from an arduino using the DHT22 sensor.

### Env vars
- AUTH_USER - user for basic auth (default to admin)
- AUTH_PASSWORD. -password for basic auth (default to admin)
- CHART_TITLE - title to show on index.html or legend of the chart (default to cigar cabinet)

Run command: `docker run -p 5000:5000 -e AUTH_USER="admin" -e AUTH_PASSWORD="admin" skykery/temp_humidity_reporter`