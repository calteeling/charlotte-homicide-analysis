import unittest
import pandas as pd
from utils import (
    filter_data,
    predict_weapon,
    get_month_name,
    get_weekday_name,
    simplify_weapon
)

class DummyModel:
    """Mock model for testing predict_weapon."""
    def predict(self, df_input):
        return ["Gun"] * len(df_input)

class TestUtils(unittest.TestCase):

    def setUp(self):
        # Sample DataFrame for filtering tests
        self.df = pd.DataFrame({
            'Year': [2022, 2023, 2023],
            'Month': [1, 2, 1],
            'Weekday': [0, 1, 0],
            'Weapon': ['Gun', 'Knife', 'Gun'],
            'Latitude': [35.2, 35.3, 35.2],
            'Longitude': [-80.8, -80.9, -80.8]
        })

    # --- filter_data ---
    def test_filter_data_all(self):
        filtered = filter_data(self.df)
        self.assertEqual(len(filtered), 3)

    def test_filter_data_specific_year(self):
        filtered = filter_data(self.df, year=2022)
        self.assertEqual(len(filtered), 1)
        self.assertEqual(filtered.iloc[0]['Year'], 2022)

    def test_filter_data_combined(self):
        filtered = filter_data(self.df, year=2023, month_label="January", weekday_label="Monday", weapon="Gun")
        self.assertEqual(len(filtered), 1)
        self.assertEqual(filtered.iloc[0]['Weapon'], "Gun")

    def test_filter_data_invalid_year(self):
        filtered = filter_data(self.df, year=1999)
        self.assertEqual(len(filtered), 0)

    # --- get_month_name ---
    def test_get_month_name_valid(self):
        self.assertEqual(get_month_name(1), "January")
        self.assertEqual(get_month_name(12), "December")

    # --- get_weekday_name ---
    def test_get_weekday_name_valid(self):
        self.assertEqual(get_weekday_name(0), "Monday")
        self.assertEqual(get_weekday_name(6), "Sunday")

    # --- predict_weapon ---
    def test_predict_weapon_mocked(self):
        df_input = pd.DataFrame([{
            'Latitude': 35.2,
            'Longitude': -80.8,
            'Age': 30,
            'Year': 2023,
            'Month': 1,
            'Weekday': 0
        }])
        model = DummyModel()
        result = predict_weapon(df_input, model)
        self.assertEqual(result[0], "Gun")

    def test_predict_weapon_multiple_rows(self):
        df_input = pd.DataFrame([
            {'Latitude': 35.2, 'Longitude': -80.8, 'Age': 30, 'Year': 2023, 'Month': 1, 'Weekday': 0},
            {'Latitude': 35.3, 'Longitude': -80.9, 'Age': 45, 'Year': 2023, 'Month': 2, 'Weekday': 1},
        ])
        model = DummyModel()
        result = predict_weapon(df_input, model)
        self.assertEqual(result, ["Gun", "Gun"])

    # --- simplify_weapon ---
    def test_simplify_weapon_gun(self):
        self.assertEqual(simplify_weapon("gun"), "Gun")
        self.assertEqual(simplify_weapon("firearm, pistol"), "Gun")
        self.assertEqual(simplify_weapon("shotgun"), "Gun")

    def test_simplify_weapon_blade(self):
        self.assertEqual(simplify_weapon("knife"), "Blade")
        self.assertEqual(simplify_weapon("razor blade"), "Blade")
        self.assertEqual(simplify_weapon("cutting instrument, sharp object"), "Blade")

    def test_simplify_weapon_other(self):
        self.assertEqual(simplify_weapon("hammer"), "Other")
        self.assertEqual(simplify_weapon(None), "Other")
        self.assertEqual(simplify_weapon(123), "Other")

if __name__ == '__main__':
    unittest.main()
