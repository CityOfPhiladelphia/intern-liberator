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

    def get_dataset(self, id):
        overview = self.scenes(self.dataset_scene).views(self.dataset_details_view).records(id).fetch()
        fields = self.views(self.dataset_details_view).fields().fetch()
        mapped_overview = self.map_fields(overview, fields)

        # Add representations
        mapped_overview['representations'] = []
        reps_qs = {'datasetdetails_id': id}
        reps = self.scenes(self.dataset_scene).views(self.dataset_reps_view).records().fetch(reps_qs)

        # Get full details for each representation
        rep_fields = self.views(self.rep_details_view).fields().fetch()
        endpoint_fields = self.views(self.rep_endpoints_view).fields().fetch()
        for rep_stub in reps['records']:
            rep_id = rep_stub['id']
            rep = self.scenes(self.rep_scene).views(self.rep_details_view).records(rep_id).fetch()
            mapped_rep = self.map_fields(rep, rep_fields)

            # Get endpoints
            endpoints_qs = {'representationdetails_id': rep_id}
            endpoints = self.scenes(self.rep_scene).views(self.rep_endpoints_view).records().fetch(endpoints_qs)
            mapped_endpoints = [self.map_fields(endpoint, endpoint_fields) for endpoint in endpoints['records']]
            mapped_rep['endpoints'] = mapped_endpoints

            mapped_overview['representations'].append(mapped_rep)

        return mapped_overview
