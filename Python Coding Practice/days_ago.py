from datetime import timedelta, date

def days_ago(n):
  return date.today() - timedelta(n)

days_ago=days_ago(5)
print(days_ago)

