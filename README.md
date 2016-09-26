# Intern Liberator
Extracts metadata records from the ([Metadata Catalog](http://metadata.phila.gov))
(a Knack application).

The goal of this project is to enable metadata to be pushed to CKAN and Socrata.

## Installation

Optionally, create a virtual environment:
```bash
virtualenv venv
```

Activate it on OSX/Linux using:
```bash
. venv/bin/activate
```
or on Windows using:
```bash
venv/Scripts/activate
```

Then install dependencies using:
```bash
pip install -r requirements.txt
```

## Usage

Output the contents of a dataset as JSON using:
```bash
python main.py <dataset-id>
```

You can pass this to a tool like [jq](https://stedolan.github.io/jq/) to
pretty-print or transform the JSON, then pipe it somewhere else, ie:
```bash
python main.py 5543ca6e5c4ae4cd66d3ff55 | jq -C   # colorize

python main.py 5543ca6e5c4ae4cd66d3ff55 | jq > trade-licenses.json
```
