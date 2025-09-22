import math
  
class Steel_can:
    def __init__(self, name, radius, height, cost):
        self.name = name
        self.radius = radius
        self.height = height
        self.cost = cost

    def volume(self):
        volume = math.pi * self.radius**2 * self.height
        return volume

    def volume_per_cost(self):
        return self.volume() / self.cost
    
    def compute_surface_area(self):
        area = 2*math.pi * self.radius * (self.radius + self.height)
        return area
    
    def compute_storage_efficiency(self):
        eff= self.volume()/ self.compute_surface_area()
        return eff
    
can1 = Steel_can("#1 Picnic", 6.83, 10.16, 0.28)
can2 = Steel_can("#1 Tall", 7.78, 11.91, 0.43)
can3 = Steel_can("#2", 8.73, 11.59, 0.45)
can4 = Steel_can("#2.5", 10.32, 11.91, 0.61)
can5 = Steel_can("#3 Cylinder", 10.79, 17.78, 0.86)
can6 = Steel_can("#5", 13.02, 14.29, 0.83)
can7 = Steel_can("#6Z", 5.40, 8.89, 0.22)
can8 = Steel_can("#8Z short", 6.83, 7.62, 0.26)
can9 = Steel_can("#10", 15.72, 17.78, 1.53)
can10 = Steel_can("#211", 6.83, 12.38, 0.34)
can11 = Steel_can("#300", 7.62, 11.27, 0.38)
can12 = Steel_can("#303", 8.10, 11.11, 0.42)


cans = [can1, can2, can3, can4, can5, can6, can7, can8, can9, can10, can11, can12]


for can in cans:
    print(f"Name: {can.name}, Volume: {can.volume():.2f}, Area: {can.compute_surface_area():.2f}")
    print(f"Storage Efficiency: {can.compute_storage_efficiency():.2f}")
    print(f"Cost: {can.cost}, Cost Efficiency: {can.volume_per_cost():.2f} \n")
    