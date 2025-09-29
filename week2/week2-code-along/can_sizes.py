import math

def main():
    can_eff("#1 Picnic", 6.83, 10.16, 0.28)
    can_eff("#1 Tall", 7.78, 11.91, 0.43)
    can_eff("#2", 8.73, 11.59, 0.45)
    can_eff("#2.5", 10.32, 11.91, 0.61)
    can_eff("#3 Cylinder", 10.79, 17.78, 0.86)
    can_eff("#5", 13.02, 14.29, 0.83)
    can_eff("#6Z", 5.40, 8.89, 0.22)
    can_eff("#8Z short", 6.83, 7.62, 0.26)
    can_eff("#10", 15.72, 17.78, 1.53)
    can_eff("#211", 6.83, 12.38, 0.34)
    can_eff("#300", 7.62, 11.27, 0.38)
    can_eff("#303", 8.10, 11.11, 0.42)

def can_eff(name, radius, height, cost):
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
