import math

def main():
    
    name = "number 1"
    radius = 6.83
    height = 10.16
    cost = 0.28

    volume = compute_volume(radius, height)
    area = compute_surface_area(radius,height)
    eff = compute_storage_efficiency(volume, area)
    cost_efficiency = compute_cost_efficiency(volume, cost)

    print(f"The cost is {cost:.2f} and the cost efficiency {cost_efficiency:.2f}")
    print(f"The {name} has a volume of {volume:.2f}")
    print(f"The area is equal {area:.2f} and the efficiency is {eff:.2f}")
    

def compute_volume(radius, height):
    volume = math.pi * radius**2 * height
    return volume

def compute_surface_area(radius, height):
    area = 2*math.pi * radius * (radius + height)
    return area


def compute_storage_efficiency(volume, area):
    efficiency = volume/area
    return efficiency

def compute_cost_efficiency(volume, cost):
    cost_eff = volume / cost
    return cost_eff

main()
