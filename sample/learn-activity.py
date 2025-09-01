"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart’s maximum rate.
"""

user = int(input("Please enter your age: "))
rate = 220 - user
minimum = (rate*65)/100
maximum = (rate*85)/100

print(f"When exercising to strengthen your heart, you should keep your rate between {minimum:.0f} and {maximum:.0f} of your hearts maximum rate")