# Add our dependencies.
from cgi import print_environ_usage
import csv
import os

# Add a variable to load a file from a path.
# file_to_load = os.path.join("Resources","election_results (1).csv")
file_to_load = open("Resources\election_results.csv")

with open(file_to_load) as fp:
    reader = csv.reader(fp, delimiter=",", quotechar='"')
    # next(reader, None)  # skip the headers
    data_read = [row for row in reader]

print(data_read)
