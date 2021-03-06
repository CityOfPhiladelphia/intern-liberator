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

Finally, copy `.env.sample` to `.env` and fill in the environment variables.
You can find the Knack Application ID by inspecting the headers of network
requests when viewing a public Knack application (requires no special access).

## Usage

Output the contents of a dataset as JSON using:
```bash
python main.py getdataset <dataset-id> [--format=ckan]
```

You can pass this to a tool like [jq](https://stedolan.github.io/jq/) to
pretty-print or transform the JSON, then pipe it somewhere else, ie:
```bash
python main.py getdataset 5543ca6e5c4ae4cd66d3ff55 | jq '.'

python main.py getdataset 5543ca6e5c4ae4cd66d3ff55 | jq '.' > trade-licenses.json

python main.py getdataset 5543ca6e5c4ae4cd66d3ff55 --format ckan | ckanapi action package_patch -i -r <hostname> -a <apikey>
```
