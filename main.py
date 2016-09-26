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
    )

@click.command()
@click.argument('id')
def getdataset(id):
    result = benny.get_dataset(id)
    print(json.dumps(result))

if __name__ == '__main__':
    getdataset()
