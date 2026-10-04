print("===========================")
print("      Travel Planner    ")
print("===========================")
destination = input("Enter your destination: ")
distance = float(input("Enter the distance in kilometers: "))
speed = float(input("Enter the approximate speed in km/h: "))

time = distance/speed

hours = int(time)
minutes = int((time-hours)*60)

print("Destination: ", destination)
print("Distance: ", distance, "km")
print("Average Speed: ", speed, "km/h")

print()

print("Estimated Travel Time: ", hours, "hours", minutes, "minutes")
# print("                     :  ", time*60, "minutes")


