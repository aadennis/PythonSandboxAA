# pip install folium
from folium import folium as f
import folium

print(folium.__file__)


f.Map(location = (51,0), zoom_start = 10).save("c:/temp/londonx2.html")

