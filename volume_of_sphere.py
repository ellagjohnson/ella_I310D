def compute_area_of_circle(radius):
	pi = 3.14
	volume = (4/3) * pi * radius ** 3
	return volume

radius1 = 30
volume1 = compute_volume_of_sphere(radius1)
print(f"The volume of sphere with radius {radius1} is: {volume1}")

radius2 = 40
volume2 = compute_volume_of_sphere(radius2)
print(f"The volume of sphere with radius {radius2} is: {volume2}")
