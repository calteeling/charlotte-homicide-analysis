# Charlotte Homicide Analysis Tools

This project provides interactive tools for exploring and analyzing homicide data in Charlotte, NC. It includes a Streamlit app with:

- A heatmap tab to visualize spatial patterns
- A prediction tool to estimate likely weapon type based on incident data
- A marker-based map for viewing individual case details

The data is sourced from the Charlotte Open Data API and includes fallback mechanisms to ensure offline availability.

## Preview

Below are example screenshots from the Charlotte Homicide Analysis Tools web app:

### Heatmap Tab
![Heatmap](screenshots/heatmap.png)

### Prediction Tool
![Prediction Tool](screenshots/prediction_tool.png)

### Marker Map
![Marker Map](screenshots/marker_map.png)

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
- Jupyter Notebooks (for development)
- Charlotte Open Data API (JSON)

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

## Data Source

The data used in this project comes from the [Charlotte Open Data Portal](https://data.charlottenc.gov/)(specifically the https://data.charlottenc.gov/datasets/charlotte::cmpd-homicide/) which provides crime incident information through a public API. To ensure reliability, a backup dataset is included in the project.

## Insights
Overall, I'm really happy with how this project turned out. I tried to create a comprehensive data analysis project, and I believe it's quite functional. It’s worth mentioning that the machine learning component is very basic. This is mainly due to the dataset being heavily weighted toward 'gun'-based entries. As a result, the prediction tool tends to rely heavily on predicting 'gun' and rarely returns 'blade' or 'other'.

If I were to do this project over again, I would probably take more time to separate the weapon classes — for example, distinguishing between handguns and rifles. However, I chose not to do this to avoid cluttering the app with too many options.

I'm also really happy with how the data functionality turned out. From the beginning, it was important to me that the project could access up-to-date data through the API. In case something goes wrong with the API, the app includes two fallback options: one using the most recent saved JSON file, and another using an archived version of the dataset.

## License

This project is licensed under the MIT License.

## Author

Developed by Cal Teeling as part of a data science portfolio project.
