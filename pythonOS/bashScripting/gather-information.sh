#!/bin/bash

echo "Starting at: $(date)"; echo

echo "UPTIME"; uptime; echo

echo "FREE"; free -h ; echo

echo "WHO"; who; echo

echo "Finishing at: $(date)"



line="-------------------------------------------------"

echo "Starting at: $(date)"; echo $line

echo "UPTIME"; uptime; echo $line

echo "FREE"; free; echo $line

echo "WHO"; who; echo $line

echo "Finishing at: $(date)"
