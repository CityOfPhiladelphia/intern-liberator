from knack import Knack

class Benny(Knack):
    def __init__(self, **kwargs):
        super(Benny, self).__init__(**kwargs)
        self.dataset_scene = kwargs['dataset_scene']
        self.dataset_details_view = kwargs['dataset_details_view']
        self.dataset_reps_view = kwargs['dataset_reps_view']
        self.rep_scene = kwargs['rep_scene']
        self.rep_details_view = kwargs['rep_details_view']
        self.rep_endpoints_view = kwargs['rep_endpoints_view']
        self.rep_fields_view = kwargs['rep_fields_view']

    def get_dataset(self, id):
        dataset = self.scenes(self.dataset_scene).views(self.dataset_details_view).records(id).fetch()
        dataset_fields = self.views(self.dataset_details_view).fields().fetch()
        mapped_dataset = self.map_fields(dataset, dataset_fields)

        # Add representations
        mapped_dataset['representations'] = []
        reps_qs = {'datasetdetails_id': id}
        reps = self.scenes(self.dataset_scene).views(self.dataset_reps_view).records().fetch(reps_qs)

        # Get full details for each representation
        rep_fields = self.views(self.rep_details_view).fields().fetch()
        endpoint_fields = self.views(self.rep_endpoints_view).fields().fetch()
        fields_fields = self.views(self.rep_fields_view).fields().fetch()
        for rep_stub in reps['records']:
            rep_id = rep_stub['id']
            rep = self.scenes(self.rep_scene).views(self.rep_details_view).records(rep_id).fetch()
            mapped_rep = self.map_fields(rep, rep_fields)

            # Get endpoints
            endpoints_qs = {'representationdetails_id': rep_id} # also used for fields
            endpoints = self.scenes(self.rep_scene).views(self.rep_endpoints_view).records().fetch(endpoints_qs)
            mapped_endpoints = [self.map_fields(endpoint, endpoint_fields) for endpoint in endpoints['records']]
            mapped_rep['endpoints'] = mapped_endpoints

            # Get representation fields (the DB columns, not knack field names)
            fields = self.scenes(self.rep_scene).views(self.rep_fields_view).records().fetch(endpoints_qs)
            mapped_fields = [self.map_fields(field, fields_fields) for field in fields['records']]
            mapped_rep['fields'] = mapped_fields

            mapped_dataset['representations'].append(mapped_rep)

        return mapped_dataset
