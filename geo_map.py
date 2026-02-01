import folium

def create_geo_map(ip_info, filename="email_origin_map.html"):
    """Generate an HTML map based on geolocation info."""
    ip = ip_info.get("IP", "Unknown")
    city = ip_info.get("City", "Unknown")
    region = ip_info.get("Region", "Unknown")
    country = ip_info.get("Country", "Unknown")
    latitude = ip_info.get("Latitude", 0)  # Replace these with actual lat/lon if available
    longitude = ip_info.get("Longitude", 0)

    # Check if latitude and longitude are valid for mapping
    if latitude and longitude and latitude != 0 and longitude != 0:
        # Create a map centered at the IP location
        m = folium.Map(location=[latitude, longitude], zoom_start=10)
        folium.Marker(
            [latitude, longitude],
            popup=f"{ip} - {city}, {region}, {country}",
            tooltip="Location"
        ).add_to(m)

        # Save the map as an HTML file
        m.save(filename)
        return filename  # Return the name of the generated HTML file
    else:
        return None  # Return None if mapping is not possible