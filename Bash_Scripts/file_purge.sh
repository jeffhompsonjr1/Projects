#!/bin/bash
set -e

cd /tmp || exit 1

# Create archive containing both directories
tar -czvf (replace_with_filename)$(date '+%Y%m%d_%H%M%S').tar.gz (insert file path)

# Purge logs
rm -rf (insert log file paths to purge)*

echo "Test logs purged successfully on $(date '+%Y-%m-%d %H:%M:%S')"


----------notes for crontab--------
crontab -e (as root)

59 23 * * 5 /opt/log_cleaner.sh

