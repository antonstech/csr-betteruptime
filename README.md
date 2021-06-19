# csr-betteruptime
This Script is for automatically connecting to a webhook and updating the Webhook description for the https://betteruptime.com Service with the Free Disk Space on the Machine it is running on.
# Cronjob Setup: 
`sudo crontab -e`   
*/5 * * * * /usr/bin/python3 /path/to/the/main.py/file
