import streamlit as st
import pandas as pd
import folium
from folium.plugins import HeatMap
from streamlit_folium import st_folium
import joblib
from utils import filter_data, predict_weapon, get_month_name, get_weekday_name, simplify_weapon

st.set_page_config(layout="wide")

if 'first_run_done' not in st.session_state:
    st.session_state.first_run_done = True
    st.rerun()

st.markdown("""
    <style>
        html, body, .main, .block-container {
            margin: 0;
            padding: 0;
            height: 100%;
            overflow: hidden;
        }
        .block-container {
            padding-left: 3rem !important;
            padding-right: 3rem !important;
            padding-top: 1rem;
            padding-bottom: 1rem;
        }
        .element-container {
            margin-bottom: 0 !important;
        }
        section[data-testid="stSidebar"] {
            padding-top: 0;
        }
    </style>
""", unsafe_allow_html=True)

st.title("Charlotte Homicide Analysis Tools")

# Load data and model
df = pd.read_csv("data/homicide_cleaned.csv", parse_dates=["Incident_Date"])
df = df.dropna(subset=["Latitude", "Longitude"])
model = joblib.load('models/model_09v4.pkl')
df['Weapon_Simplified'] = df['Weapon'].apply(simplify_weapon)

# Extract date parts
df["Year"] = df["Incident_Date"].dt.year
df["Month"] = df["Incident_Date"].dt.month
df["Weekday"] = df["Incident_Date"].dt.dayofweek

month_labels = {i: get_month_name(i) for i in range(1, 13)}
weekday_labels = {i: get_weekday_name(i) for i in range(7)}

page = st.radio("Navigation", ["Heatmap", "Prediction Tool", "All Markers Map"], horizontal=True)

# Tab 1 - Heatmap
if page == 'Heatmap':
    with st.sidebar:
        st.header("Filter Options")
        if st.button('Reset Filters'):
            st.session_state['year_filter'] = 'All'
            st.session_state['month_filter'] = 'All'
            st.session_state['weekday_filter'] = 'All'
            st.session_state['weapon_filter'] = 'All'

        year = st.selectbox("Year", options=["All"] + sorted(df["Year"].dropna().unique().tolist()), key='year_filter')
        month = st.selectbox("Month", options=["All"] + list(month_labels.values()), key='month_filter')
        weekday = st.selectbox("Weekday", options=["All"] + list(weekday_labels.values()), key='weekday_filter')
        weapon = st.selectbox("Weapon", options=["All"] + sorted(df["Weapon"].dropna().unique().tolist()), key='weapon_filter')

    filtered_df = filter_data(df, year, month, weekday, weapon)
    st.write(f"Showing {len(filtered_df)} records after filtering.")
    st.markdown('Map Display Options')
    reset_view = st.button('Reset View')

    def plot_heatmap(df_subset, center=None, zoom=12):
        if df_subset.empty:
            return folium.Map(location=[35.2271, -80.8431], zoom_start=12)
        heat_data = df_subset[['Latitude', 'Longitude']].dropna().values.tolist()
        if center is None:
            center = [df_subset['Latitude'].mean(), df_subset['Longitude'].mean()]
        m = folium.Map(location=center, zoom_start=zoom, tiles='OpenStreetMap')
        HeatMap(heat_data, radius=20, blur=15, min_opacity=0.45, max_zoom=16).add_to(m)
        return m

    map_center = [35.2271, -80.8431]
    if not reset_view and not filtered_df.empty:
        try:
            map_center = filtered_df[['Latitude', 'Longitude']].mean().values.tolist()
        except:
            pass
    map_zoom = 12

    if filtered_df.empty:
        st.warning("No incidents found for this combination.")
    else:
        m = plot_heatmap(filtered_df, center=map_center, zoom=map_zoom)
        st_folium(m, width=1100, height=550)

# Tab 2 - Prediction Tool
elif page == 'Prediction Tool':
    st.subheader('Predict Weapon Type Based on Scenario')
    col1, col2 = st.columns(2)

    with col1:
        age = st.slider('Victim Age', 10, 100, 30)
        year_input = st.selectbox('Year', sorted(df['Year'].unique()))
        month_label = st.selectbox('Month', list(month_labels.values()))
        month_input = [num for num, label in month_labels.items() if label == month_label][0]
        weekday_label = st.selectbox('Weekday', list(weekday_labels.values()))
        weekday_input = [num for num, label in weekday_labels.items() if label == weekday_label][0]

    with col2:
        st.markdown('Click on the map to choose a location')
        mini_map = folium.Map(location=[35.2271, -80.8431], zoom_start=11)
        mini_map.add_child(folium.LatLngPopup())
        map_data = st_folium(mini_map, height=400, width=700)

        if map_data and map_data.get('last_clicked'):
            lat = map_data['last_clicked']['lat']
            lon = map_data['last_clicked']['lng']
            st.success(f'Selected Location: ({lat:.5f}, {lon:.5f})')
        else:
            lat = None
            lon = None
            st.warning('Click on the map to select location')

    if lat is not None and lon is not None:
        input_df = pd.DataFrame([{
            'Latitude': lat,
            'Longitude': lon,
            'Age': age,
            'Year': year_input,
            'Month': month_input,
            'Weekday': weekday_input
        }])
        if st.button('Predict Weapon'):
            pred = predict_weapon(input_df, model)[0]
            st.success(f'Predicted Weapon: **{pred}**')
    else:
        st.info('Waiting for location input from the map...')

# Tab 3 - All Markers Map
elif page == 'All Markers Map':
    with st.sidebar:
        st.header("Filter Options")
        weapon_filter = st.selectbox("Weapon Category", ["All", "Gun", "Blade", "Other"])
        st.markdown("---")
        st.markdown("### Marker Legend")
        st.markdown("""
        - 🔴 **Gun**  
        - 🔵 **Blade**  
        - 🟢 **Other**
        """)

    filtered_df = df.copy()
    if weapon_filter != "All":
        filtered_df = filtered_df[filtered_df["Weapon_Simplified"] == weapon_filter]

    st.write(f"Showing {len(filtered_df)} incidents.")
    st.markdown('Map Display Options')
    reset_view = st.button('Reset View')

    map_center = [35.2271, -80.8431]
    if not reset_view and not filtered_df.empty:
        try:
            map_center = filtered_df[['Latitude', 'Longitude']].mean().values.tolist()
        except:
            pass
    map_zoom = 12
    marker_map = folium.Map(location=map_center, zoom_start=map_zoom)

    for _, row in filtered_df.iterrows():
        location = [row['Latitude'], row['Longitude']]
        simplified = row['Weapon_Simplified']
        if simplified == 'Gun':
            color = 'red'
        elif simplified == 'Blade':
            color = 'blue'
        else:
            color = 'green'
        popup_content = f"""
        <b>Date:</b> {row['Incident_Date'].date()}<br>
        <b>Weapon:</b> {row['Weapon']}<br>
        <b>NPA:</b> {row['NPA']}<br>
        <b>Victim Age:</b> {row['Age']}<br>
        <b>Category:</b> {simplified}
        """
        folium.Marker(
            location=location,
            popup=folium.Popup(popup_content, max_width=300),
            icon=folium.Icon(color=color)
        ).add_to(marker_map)

    st_folium(marker_map, width=1100, height=550)
