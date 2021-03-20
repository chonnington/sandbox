

class ExtractAndSumScore(beam.PTransform):

    """
    A transform to extract key/score information and sum the scores.
    The constructor argument `field` determines whether 'team' or 'user' info is
    extracted.
    """
  
    def __init__(self, field):
        beam.PTransform.__init__(self)
        self.field = field

    def expand(self, pcoll):
        return (
            pcoll
            | beam.Map(lambda elem: (elem[self.field], elem['score']))
            | beam.CombinePerKey(sum)
        )
    
    
def run(argv=None, save_main_session=True):
    
    """Main entry point; defines and runs the user_score pipeline."""
    
    parser = argparse.ArgumentParser()

    # The default maps to two large Google Cloud Storage files (each ~12GB)
    # holding two subsequent day's worth (roughly) of data.
    
    parser.add_argument(
        '--input',
        type=str,
        default='gs://apache-beam-samples/game/gaming_data*.csv',
        help='Path to the data file(s) containing game data.')
    
    parser.add_argument(
        '--output', type=str, required=True, help='Path to the output file(s).')

    args, pipeline_args = parser.parse_known_args(argv)

    options = PipelineOptions(pipeline_args)

    # We use the save_main_session option because one or more DoFn's in this
    # workflow rely on global context (e.g., a module imported at module level).
    
    options.view_as(SetupOptions).save_main_session = save_main_session

    with beam.Pipeline(options=options) as p:
        
        def format_user_score_sums(user_score):
            (user, score) = user_score
            return 'user: %s, total_score: %s' % (user, score)

        (
            p
            | 'ReadInputText' >> beam.io.ReadFromText(args.input)
            | 'UserScore' >> UserScore()
            | 'FormatUserScoreSums' >> beam.Map(format_user_score_sums)
            | 'WriteUserScoreSums' >> beam.io.WriteToText(args.output)
        )