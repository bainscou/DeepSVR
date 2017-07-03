from unittest import TestCase
from manual_review_classifier.PrepareData import PrepareData
import os

TEST_DATA_BASE_DIR = './manual_review_classifier/tests/test_data'


def file_len(fname):
    """Source: https://stackoverflow.com/q/845058/3862525"""
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1


class TestPrepareData(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.samples_noheader = PrepareData(os.path.join(TEST_DATA_BASE_DIR,
                                                        'samples.noheader.tsv'
                                                        ),
                                           False,
                                           os.path.join(TEST_DATA_BASE_DIR,
                                                        'training_data'))
        cls.samples_header = PrepareData(os.path.join(TEST_DATA_BASE_DIR,
                                                      'samples.tsv'),
                                         True,
                                         os.path.join(TEST_DATA_BASE_DIR,
                                                      'training_data'))

    def test__parse_samples_file(self):
        self.assertTrue(len(self.samples_header.samples) == 1)
        self.assertTrue(len(self.samples_noheader.samples) == 1)

    def test__run_bam_readcount(self):
        self.assertEqual(file_len(os.path.join(TEST_DATA_BASE_DIR,
                                               'training_data', 'readcounts',
                                               'tst1_normal.readcounts')),
                         443)
        self.assertEqual(file_len(os.path.join(TEST_DATA_BASE_DIR,
                                               'training_data', 'readcounts',
                                               'tst1_tumor.readcounts')),
                         443)
        self.assertEqual(len(self.samples_noheader.training_data), 443)
        self.assertEqual(len(self.samples_noheader.training_data.columns), 60)
        self.assertEqual(
            round(self.samples_noheader.training_data.values.max(), 3), 1)