from datetime import datetime, timedelta

# Define a function to approximate tide times and heights based on Full Moon
def approximate_tide_data(full_moon_date, seed_time, high_water_height, low_water_height):
    # Convert Full Moon date to a datetime object
    full_moon = datetime.strptime(full_moon_date, "%Y-%m-%d")

    # Calculate time difference between Full Moon and seed time
    time_difference = seed_time - full_moon

    # Approximate high tide time
    high_tide_time = full_moon + time_difference
    # Approximate low tide time (assuming a 6-hour time difference between high and low tide)
    low_tide_time = high_tide_time + timedelta(hours=6)

    # Approximate tide heights based on seed heights
    high_tide_height = high_water_height
    low_tide_height = low_water_height

    # Print the approximate tide data
    print("Approximate Tide Data:")
    print("High Tide: ", high_tide_time.strftime("%Y-%m-%d %H:%M"))
    print("High Water Height: ", high_tide_height)
    print("Low Tide: ", low_tide_time.strftime("%Y-%m-%d %H:%M"))
    print("Low Water Height: ", low_tide_height)

# Example usage
full_moon_date = "2023-07-15"
seed_time = datetime(2023, 7, 10, 12, 0)  # Seed time for estimation
high_water_height = 3.5  # Example high water height
low_water_height = 1.2  # Example low water height

approximate_tide_data(full_moon_date, seed_time, high_water_height, low_water_height)
