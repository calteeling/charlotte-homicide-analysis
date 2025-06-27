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

## Data Source

The data used in this project comes from the [Charlotte Open Data Portal](https://data.charlottenc.gov/)(specifically the https://data.charlottenc.gov/datasets/charlotte::cmpd-homicide/) which provides crime incident information through a public API. To ensure reliability, a backup dataset is included in the project.

## Insights
Overall, I'm really happy with how this project turned out. I tried to create an encompasing data analysis project and I believe that it's quite functional. It is worth mentioning that the ML is very basic. This mainly comes from the fact that the dataset I used is heavily weighted towards 'gun' based entries. This causes an extreme reliance on 'gun' predictions for the prediction tool as it rarely returns 'blade' or 'other'. If I had to do this project over again I would probably take more time separating the weapon classes such as hanguns and rifles being in two classes, but I didnt want the app to become too cluttered with options. 

I'm also really happy with the functionlity of the data. When I started the project, it was really important for it to have updated data that it uses from the API. In case something goes wrong with the API, there are two fallbacks, one being the most recent json, and two being the archieved json.

## License

This project is licensed under the MIT License.

## Author

Developed by Cal Teeling as part of a data science portfolio project.
