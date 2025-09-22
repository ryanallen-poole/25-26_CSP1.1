import datetime as dt
user_name = input("What is your name? ")
print("Hello", user_name, "welcome to my program.")
age=input("How old are you? ")
curr_year=dt.datetime.today().year
birth_year=curr_year-int(age)
print(Hmmm. . . were you bron in", birth_year, ".")")