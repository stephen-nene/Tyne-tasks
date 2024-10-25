#!/bin/bash

# Define the IP range based on your network
IP_RANGE="192.168.1.0/24"

# Output file
OUTPUT_FILE="detailed_scan.txt"

# Step 1: Run Nmap ping scan to detect all live hosts
echo "Performing ping scan to detect live hosts..."
nmap -sn $IP_RANGE -oG - | awk '/Up$/{print $2}' > live_hosts.txt

# Count the number of live hosts found
NUM_HOSTS=$(wc -l < live_hosts.txt)
echo "Performed ping scan to detect live hosts and found $NUM_HOSTS hosts."

# Step 2: Perform a detailed Nmap scan on the detected live hosts if any are found
if [ $NUM_HOSTS -gt 0 ]; then
    echo "Performing detailed scan on $NUM_HOSTS live hosts..."
    nmap -A -iL live_hosts.txt -oN $OUTPUT_FILE
    echo "Detailed scan complete. Results saved to $OUTPUT_FILE."
else
    echo "No live hosts found. Skipping detailed scan."
fi
