#!/usr/bin/env bash
# Watchdog: stop machine when no SSH sessions are active
# Grace period: wait for first connection before watching
sleep 60
while true; do
  sleep 30
  if ! ss -tnp | grep -q ':22 '; then
    poweroff
  fi
done
