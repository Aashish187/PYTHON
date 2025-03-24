# Storing The Value
from pathlib import Path
import json
fav_num=int(input("Enter Your Favourite Number: "))
path=Path('fav_num.json')
# stores the number in json file
contents=json.dumps(fav_num)
path.write_text(contents)


# Reading The Stored Value
from pathlib import Path
import json
path=Path('fav_num.json')
contents=path.read_text()
fav_num=json.loads(contents)
print(f"I Know Your Favourite Number! It's {fav_num}")