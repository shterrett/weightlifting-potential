import unittest

from weightlifting import import_data as data

class TestImport(unittest.TestCase):
    def test_expand_names_in_atg_data(self):
        atg_df = data.import_atg()
        martin = atg_df[atg_df.Name == "Martin Tesovic"]
        self.assertEqual(martin.first_name.item(), "martin")
        self.assertEqual(martin.last_name.item(), "tesovic")

    def test_expand_names_in_iwf_data(self):
        iwf_df = data.import_iwf()
        martin = iwf_df[iwf_df.name == "TESOVIC Martin"]
        self.assertEqual(martin.first_name.item(), "martin")
        self.assertEqual(martin.last_name.item(), "tesovic")

    def test_build_joined_data_frame(self):
        full_data = data.build_joined_data_frame()
        martin = full_data[(full_data.first_name == "martin") &
                           (full_data.last_name == "tesovic")]
        self.assertEqual(martin.height.item(), 182)
        self.assertEqual(martin.weight.item(), 104.19)
        self.assertEqual(martin.snatch.item(), 167)
        self.assertEqual(martin.cj.item(), 196)
        self.assertEqual(martin.category.item(), 105)
