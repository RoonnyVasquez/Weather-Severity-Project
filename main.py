def main():
    readings = [0.2, 25, 1.0, 35, 4.5, 45]
    total_rain = 0
    total_wind = 0
    count = 0

    for i in range(0, len(readings), 2):
        rain = readings[i]
        wind = readings[i + 1]

        total_rain += rain
        total_wind += wind
        count += 1

    average_rain = total_rain / count
    average_wind = total_wind / count

    weather_severity = (average_wind * 1.5) + average_rain

    print(f"The average rain is {average_rain:.1f} inches")
    print(f"The average wind is {average_wind:.1f} mph")
    print(f"The weather severity for these {count} readings is: {weather_severity:.1f}")


if __name__ == "__main__":
    main()