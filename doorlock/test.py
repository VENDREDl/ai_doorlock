
import googlemaps
import folium

gmaps_key = "AIzaSyD1a21VhXwzKX6lyJHuAjBJTfTPHhJy81o"

gmaps = googlemaps.Client(key=gmaps_key)

a = gmaps.geocode('대한민국 서울특별시 강남구 대치2동 514', language="ko")

print(a)

b = folium.Map(location=[35.1657, 129.0725], zoom_start=20)

c = folium.Marker(location=[35.1657, 129.0725], popup='동의과학대', icon=folium.Icon(icon='cloud')).add_to(b)

b.save('./test.html')

# lat': 35.165777, 129.072536