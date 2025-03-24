from pathlib import Path
import json
username=input("Enter Your Name: ")
age=int(input("Enter Your Age: "))
movie=input("Enter Your Favourite Movie: ")
info={'username':username,'age':age,'movie':movie}
path=Path('info.json')
contents=json.dumps(info)
path.write_text(contents)

#These are 2 diffrent codes one for storing data in json and one for showing data stored in json

#  READING THE STORED DATA
from pathlib import Path
import json
path=Path("info.json")
contents=path.read_text()
info=json.loads(contents)
print(f"You are {info["username"].title()} and your age is {info["age"]} and your favourite movie is {info["movie"].title()}")