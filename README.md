# Data Visualization
This repository provides a Python script to visualize machine tool signature data from a set of CSV and ZIP files. The script processes the data, dynamically generates subplots, and displays the results in a comprehensible format.
## Features
* Reads .csv files for metadata (e.g., filenames, timestamps).
* Processes .zip files containing time-series data for various dimensions.
* Dynamically calculates the required number of subplots based on the data dimensions.
* Visualizes each dimension's data with corresponding timestamps.
* Automatically adds legends, grids, and axis labels for better readability.
## Requirements
Python: 3.11
## Libraries:
* pandas
* matplotlib
* pathlib
* math
