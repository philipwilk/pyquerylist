from pathlib import Path
import runpy

class TestExamples:

    def test_examples(self):
        examples = Path(__file__).parent.parent / 'pyquerylist' / 'examples.py'
        # Make sure that if __name__ == '__main__': block is run.
        examples_results = runpy.run_path(examples, run_name='__main__')
        assert 'books' in examples_results
