import os
import sys
import json
from copy import copy

import click
from dotenv import load_dotenv

from benny import Benny

# Load environment variables
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

benny = Benny(
    application_id=os.environ.get('KNACK_APPLICATION_ID'),
    dataset_scene=os.environ.get('DATASET_SCENE'),
    dataset_details_view=os.environ.get('DATASET_DETAILS_VIEW'),
    dataset_reps_view=os.environ.get('DATASET_REPRESENTATIONS_VIEW'),
    rep_scene=os.environ.get('REPRESENTATION_SCENE'),
    rep_details_view=os.environ.get('REPRESENTATION_DETAILS_VIEW'),
    rep_endpoints_view=os.environ.get('REPRESENTATION_ENDPOINTS_VIEW'),
    rep_fields_view=os.environ.get('REPRESENTATION_FIELDS_VIEW')
    )

@click.group()
def cli():
    pass

@cli.command()
@click.argument('id')
@click.option('--format', help='optional output format (ie. ckan)')
def getdataset(id, format=''):
    result = benny.get_dataset(id)
    if format == 'ckan':
        ckan_result = benny.to_ckan(result)
        click.echo(json.dumps(ckan_result))
    else:
        click.echo(json.dumps(result))

@cli.command()
def tockan():
    input_data = json.load(sys.stdin)
    ckan_result = benny.to_ckan(input_data)
    click.echo(json.dumps(ckan_result))

if __name__ == '__main__':
    cli()
