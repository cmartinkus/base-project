#!/bin/sh

# tells the script to exit immediately if a command fails, so you don't accidentally start Nginx with a bad configuration.
set -e

cat <<EOF >/usr/share/nginx/html/config.js
window.__APP_CONFIG__ = {
    API_URL: "${API_URL}",
    APP_NAME: "${APP_NAME}"
}
EOF

exec nginx -g "daemon off;"