# Charlotte Homicide Analysis Tools

This project provides interactive tools for exploring and analyzing homicide data in Charlotte, NC. It includes a Streamlit app with:

- A heatmap tab to visualize spatial patterns
- A prediction tool to estimate likely weapon type based on incident data
- A marker-based map for viewing individual case details

The data is sourced from the Charlotte Open Data API and includes fallback mechanisms to ensure offline availability.

## Features

- Interactive filtering by year, month, weekday, and weapon type
- Machine learning prediction model for weapon classification
- Dynamic heatmaps and popup-rich marker maps
- API integration with automatic fallback to local data
- Modular code structure with unit tests

## Tech Stack

- Python
- Streamlit
- Pandas
- Folium
- Scikit-learn (for ML model)
- JSON API from the Charlotte Open Data Portal

## Features

- Interactive heatmap of homicide incidents by year, month, weekday, and weapon
- Sidebar filtering for customized analysis
- Predictive tool that estimates weapon type from input features
- Unit-tested utility functions for robustness
- Modular structure with Jupyter notebooks, models, and fallback data

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/charlotte-homicide-tools.git
   cd charlotte-homicide-tools
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv myenv
   source myenv/bin/activate   # Windows: myenv\Scripts\activate
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Running the App

To launch the app in your browser:

```bash
streamlit run app.py
```
If the Charlotte crime API is unavailable, the app will automatically fall back to using local JSON or CSV files in the `data/` directory.

## Testing

To run all unit tests:

```bash
python -m unittest discover -s tests
```
This will verify the utility functions used for data filtering, prediction, and formatting.

## Project Structure
├── __pycache__/
│   └── utils.cpython-312.pyc
├── data/
│   ├── backup_homicide_data.json
│   ├── homicide_cleaned.csv
│   └── homicide_raw.json
├── models/
│   ├── final_fandom_forest.pkl
│   ├── label_mapping.json
│   ├── model_09v3.pkl
│   ├── model_09v4.pkl
│   ├── random_forest_weapon_classifier.pkl
│   ├── weapon_label_encoder.plk
│   ├── weapons_encoder.pkl
│   └── weapons_predictor.pkl
├── notebooks/
│   ├── 01_data_fetch.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_heatmap.ipynb
│   ├── 04_subsets.ipynb
│   ├── 05_ui.ipynb
│   ├── 06_ml.ipynb
│   ├── 07_ml_improved.ipynb
│   ├── 08_modeling.ipynb
│   ├── 09_model_refinement_evaluation.ipynb
│   ├── 09_v2_model_refinement_evaluation.ipynb
│   ├── 09_v3.ipynb
│   ├── 09_v4.ipynb
│   └── 10_app_integreation.ipynb
├── outputs/
│   ├── heat_map_knife_2022.html
│   ├── heatmap_2023.html
│   ├── heatmap_handgun.html
│   ├── heatmap_npa12.html
│   └── homicide_heatmap.html
├── tests/
│   ├── __init__.py
│   └── test_utils.py
├── .gitignore
├── README.md
├── app.py
└── requirements.txt

## Data Source

The data used in this project comes from the [Charlotte Open Data Portal](https://data.charlottenc.gov/)(specifically the https://data.charlottenc.gov/datasets/charlotte::cmpd-homicide/) which provides crime incident information through a public API. To ensure reliability, a backup dataset is included in the project.

## Insights
Overall, I'm really happy with how this project turned out. I tried to create an encompasing data analysis project and I believe that it's quite functional. It is worth mentioning that the ML is very basic. This mainly comes from the fact that the dataset I used is heavily weighted towards 'gun' based entries. This causes an extreme reliance on 'gun' predictions for the prediction tool as it rarely returns 'blade' or 'other'. If I had to do this project over again I would probably take more time separating the weapon classes such as hanguns and rifles being in two classes, but I didnt want the app to become too cluttered with options. 

I'm also really happy with the functionlity of the data. When I started the project, it was really important for it to have updated data that it uses from the API. In case something goes wrong with the API, there are two fallbacks, one being the most recent json, and two being the archieved json.

## License

This project is licensed under the MIT License.

## Author

Developed by Cal Teeling as part of a data science portfolio project.
