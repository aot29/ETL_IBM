# download access log file
wget "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Bash%20Scripting/ETL%20using%20shell%20scripting/web-server-access-log.txt.gz"

# Unzip the file to extract the .txt file.
gunzip -f web-server-access-log.txt.gz

# Extract timestamp (1), latitude (2), longitude (3) and visitorid (4)
cut -d"#" -f1-4 web-server-access-log.txt > extracted-data.txt

# Transform
tr "#" "," < extracted-data.txt > transformed-data.csv

# Load
export PGPASSWORD=XXXXXXXXXXXXX
echo "\c template1;\COPY access_log(timestamp, latitude, longitude, visitorid) FROM '/home/project/transformed-data.csv' DELIMITER ',' CSV HEADER;" | psql --username=postgres --host=postgres
