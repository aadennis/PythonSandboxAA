# pip install gpxpy pandas Pyarrow tcxparser
# pip install python-tcxparser

import tcxparser
import pandas as pd
from pathlib import Path

def tcx_to_csv(tcx_file):
    tcx_data = tcxparser.TCXParser(tcx_file)

    # Extract data from TCX
    track_points = []
    for trackpoint in tcx_data.trackpoints:
        track_points.append([trackpoint.latitude, trackpoint.longitude, trackpoint.altitude, trackpoint.time])

    # Create a DataFrame
    df = pd.DataFrame(track_points, columns=['Latitude', 'Longitude', 'Elevation', 'Time'])

    # Convert time to string format
    df['Time'] = df['Time'].astype(str)

    # Export to CSV
    csv_file = tcx_file.replace('.tcx', '_tcx.csv')
    df.to_csv(csv_file, index=False)
    print(f'CSV file saved: {csv_file}')


tcx_file = "gpx/data/jog_20240207.tcx"
tcx_to_csv(tcx_file)





