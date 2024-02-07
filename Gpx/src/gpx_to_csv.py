from pathlib import Path 
# pip install gpxpy pandas Pyarrow

import gpxpy
import pandas as pd

def gpx_to_csv(gpx_file):
    # Parse the GPX file
    print("!!!File Path:", Path(__file__).absolute())
    print("!!!Directory Path:", Path().absolute()) # Directory of current working directory, not __file__

    with open(gpx_file, 'r') as gpx:
        gpx_data = gpxpy.parse(gpx)

    # Extract data from GPX
    track_points = []
    for track in gpx_data.tracks:
        for segment in track.segments:
            for point in segment.points:
                track_points.append([point.latitude, point.longitude, point.elevation, point.time])

    # Create a DataFrame
    df = pd.DataFrame(track_points, columns=['Latitude', 'Longitude', 'Elevation', 'Time'])

    # Convert time to string format
    df['Time'] = df['Time'].astype(str)

    # Export to CSV
    csv_file = gpx_file.replace('.gpx', '.csv')
    df.to_csv(csv_file, index=False)
    print(f'CSV file saved: {csv_file}')

gpx_file = "data/jog_20240207.gpx"
gpx_to_csv(gpx_file)
