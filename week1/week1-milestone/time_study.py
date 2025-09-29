from datetime import datetime, timedelta, date


current_date_time = date.today()

print(f"{current_date_time}")
then=current_date_time + timedelta(days=30)
print(f"in 30 days it will bw {then}")
christmas = datetime(2025,12,25)
print(f"chrismas will be {christmas}")
wait=christmas - current_date_time
print(f"chrismas will be {wait}")
print(f"chrismas will be {christmas.weekday()}")

favstr = input("What is your favorite date")
favdate = datetime.strptime(favstr,"%m/%d/%Y")
diff = favdate - current_date_time
print(f" your fav date is {diff} away.")
