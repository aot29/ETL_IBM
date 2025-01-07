# This script
# Extracts data from /etc/passwd file into a CSV file.

# The csv data file contains the user name, user id and
# home directory of each user account defined in /etc/passwd

# Transforms the text delimiter from ":" to ",".
# Loads the data from the CSV file into a table in PostgreSQL database.

# Extract
echo "Extracting data"

# Extract the columns 1 (user name), 3 (user id) and 6 (home) from /etc/passwd
cut -d":" -f1,3,6 /etc/passwd > extracted-data.txt

# Transform

echo "Transforming data"

# replace colons with commas

tr ":" "," < extracted-data.txt > transformed-data.txt

# Load

echo "Loading data"

export PGPASSWORD="CUyyzD2S6HF1005AquSHWQVo;"
echo "\c template1;\COPY users  FROM '/home/project/transformed-dat>
