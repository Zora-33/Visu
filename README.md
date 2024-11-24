# Visu
This repository provides a Python script to visualize machine tool signature data from a set of CSV and ZIP files. The script processes the data, dynamically generates subplots, and displays the results in a comprehensible format.

##Features
Reads .csv files for metadata (e.g., filenames, timestamps).
Processes .zip files containing time-series data for various dimensions.
Dynamically calculates the required number of subplots based on the data dimensions.
Visualizes each dimension's data with corresponding timestamps.
Automatically adds legends, grids, and axis labels for better readability.
Requirements
Python 3.11
Libraries:
pandas
matplotlib
pathlib
math
Install the required libraries with:

bash
Code kopieren
pip install pandas matplotlib
Usage
Clone the repository and navigate to the directory:

bash
Code kopieren
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
Update the file paths in the script: Edit the read_path variable to point to your data directory:

python
Code kopieren
read_path = Path(r"C:\path\to\your\data_directory")
Place your .csv and .zip files in the specified directory.

Run the script:

bash
Code kopieren
python script_name.py
The script will generate visualizations for the data in the provided files and display them using matplotlib.

