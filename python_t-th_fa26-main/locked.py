"""
1. Constants
2. Tuples
3. Parallel lists/tuples
4. Multi Level Lists (tables)
"""

# 🔒 Constants are written in all caps.

SALES_TAX = [
    0.01,
]

# 📦 A tuple stores a sequence of values that should not change.
days_of_week = (
    "Sunday",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
)

# 🔗 Parallel tuples keep related data in separate one-dimensional tuples.
# The same row index connects the state, capital, and bird across all three.
states = (
    "Alabama",
    "Alaska",
    "Arizona",
    "Arkansas",
    "California",
    "Colorado",
    "Connecticut",
    "Delaware",
    "Florida",
    "Georgia",
    "Hawaii",
    "Idaho",
    "Illinois",
    "Indiana",
    "Iowa",
    "Kansas",
    "Kentucky",
    "Louisiana",
    "Maine",
    "Maryland",
    "Massachusetts",
    "Michigan",
    "Minnesota",
    "Mississippi",
    "Missouri",
    "Montana",
    "Nebraska",
    "Nevada",
    "New Hampshire",
    "New Jersey",
    "New Mexico",
    "New York",
    "North Carolina",
    "North Dakota",
    "Ohio",
    "Oklahoma",
    "Oregon",
    "Pennsylvania",
    "Rhode Island",
    "South Carolina",
    "South Dakota",
    "Tennessee",
    "Texas",
    "Utah",
    "Vermont",
    "Virginia",
    "Washington",
    "West Virginia",
    "Wisconsin",
    "Wyoming",
)

state_capitals = (
    "Montgomery",
    "Juneau",
    "Phoenix",
    "Little Rock",
    "Sacramento",
    "Denver",
    "Hartford",
    "Dover",
    "Tallahassee",
    "Atlanta",
    "Honolulu",
    "Boise",
    "Springfield",
    "Indianapolis",
    "Des Moines",
    "Topeka",
    "Frankfort",
    "Baton Rouge",
    "Augusta",
    "Annapolis",
    "Boston",
    "Lansing",
    "Saint Paul",
    "Jackson",
    "Jefferson City",
    "Helena",
    "Lincoln",
    "Carson City",
    "Concord",
    "Trenton",
    "Santa Fe",
    "Albany",
    "Raleigh",
    "Bismarck",
    "Columbus",
    "Oklahoma City",
    "Salem",
    "Harrisburg",
    "Providence",
    "Columbia",
    "Pierre",
    "Nashville",
    "Austin",
    "Salt Lake City",
    "Montpelier",
    "Richmond",
    "Olympia",
    "Charleston",
    "Madison",
    "Cheyenne",
)

state_birds = (
    "Yellowhammer",
    "Willow ptarmigan",
    "Cactus wren",
    "Northern mockingbird",
    "California quail",
    "Lark bunting",
    "American robin",
    "Blue hen chicken",
    "Northern mockingbird",
    "Brown thrasher",
    "Hawaiian goose",
    "Mountain bluebird",
    "Northern cardinal",
    "Northern cardinal",
    "Eastern goldfinch",
    "Western meadowlark",
    "Northern cardinal",
    "Brown pelican",
    "Black-capped chickadee",
    "Baltimore oriole",
    "Black-capped chickadee",
    "American robin",
    "Common loon",
    "Northern mockingbird",
    "Eastern bluebird",
    "Western meadowlark",
    "Western meadowlark",
    "Mountain bluebird",
    "Purple finch",
    "Eastern goldfinch",
    "Greater roadrunner",
    "Eastern bluebird",
    "Northern cardinal",
    "Western meadowlark",
    "Northern cardinal",
    "Scissor-tailed flycatcher",
    "Western meadowlark",
    "Ruffed grouse",
    "Rhode Island Red",
    "Carolina wren",
    "Ring-necked pheasant",
    "Northern mockingbird",
    "Northern mockingbird",
    "California gull",
    "Hermit thrush",
    "Northern cardinal",
    "American goldfinch",
    "Northern cardinal",
    "American robin",
    "Western meadowlark",
)

# 🧱 A nested tuple groups each state's values into one row.
# The outer tuple holds rows; each inner tuple has two columns:
# column [0] is the state and column [1] is the capital.
states_and_capitals = (
    ("Alabama", "Montgomery"),
    ("Alaska", "Juneau"),
    ("Arizona", "Phoenix"),
    ("Arkansas", "Little Rock"),
    ("California", "Sacramento"),
    ("Colorado", "Denver"),
    ("Connecticut", "Hartford"),
    ("Delaware", "Dover"),
    ("Florida", "Tallahassee"),
    ("Georgia", "Atlanta"),
    ("Hawaii", "Honolulu"),
    ("Idaho", "Boise"),
    ("Illinois", "Springfield"),
    ("Indiana", "Indianapolis"),
    ("Iowa", "Des Moines"),
    ("Kansas", "Topeka"),
    ("Kentucky", "Frankfort"),
    ("Louisiana", "Baton Rouge"),
    ("Maine", "Augusta"),
    ("Maryland", "Annapolis"),
    ("Massachusetts", "Boston"),
    ("Michigan", "Lansing"),
    ("Minnesota", "Saint Paul"),
    ("Mississippi", "Jackson"),
    ("Missouri", "Jefferson City"),
    ("Montana", "Helena"),
    ("Nebraska", "Lincoln"),
    ("Nevada", "Carson City"),
    ("New Hampshire", "Concord"),
    ("New Jersey", "Trenton"),
    ("New Mexico", "Santa Fe"),
    ("New York", "Albany"),
    ("North Carolina", "Raleigh"),
    ("North Dakota", "Bismarck"),
    ("Ohio", "Columbus"),
    ("Oklahoma", "Oklahoma City"),
    ("Oregon", "Salem"),
    ("Pennsylvania", "Harrisburg"),
    ("Rhode Island", "Providence"),
    ("South Carolina", "Columbia"),
    ("South Dakota", "Pierre"),
    ("Tennessee", "Nashville"),
    ("Texas", "Austin"),
    ("Utah", "Salt Lake City"),
    ("Vermont", "Montpelier"),
    ("Virginia", "Richmond"),
    ("Washington", "Olympia"),
    ("West Virginia", "Charleston"),
    ("Wisconsin", "Madison"),
    ("Wyoming", "Cheyenne"),
)

# 📊 A three-column nested tuple represents a table of related records.
# The outer tuple contains rows; each inner tuple contains one row's columns.
# Each row has three columns: state [0], capital [1], and state bird [2].
states_capitals_birds = (
    ("Alabama", "Montgomery", "Yellowhammer"),
    ("Alaska", "Juneau", "Willow ptarmigan"),
    ("Arizona", "Phoenix", "Cactus wren"),
    ("Arkansas", "Little Rock", "Northern mockingbird"),
    ("California", "Sacramento", "California quail"),
    ("Colorado", "Denver", "Lark bunting"),
    ("Connecticut", "Hartford", "American robin"),
    ("Delaware", "Dover", "Blue hen chicken"),
    ("Florida", "Tallahassee", "Northern mockingbird"),
    ("Georgia", "Atlanta", "Brown thrasher"),
    ("Hawaii", "Honolulu", "Hawaiian goose"),
    ("Idaho", "Boise", "Mountain bluebird"),
    ("Illinois", "Springfield", "Northern cardinal"),
    ("Indiana", "Indianapolis", "Northern cardinal"),
    ("Iowa", "Des Moines", "Eastern goldfinch"),
    ("Kansas", "Topeka", "Western meadowlark"),
    ("Kentucky", "Frankfort", "Northern cardinal"),
    ("Louisiana", "Baton Rouge", "Brown pelican"),
    ("Maine", "Augusta", "Black-capped chickadee"),
    ("Maryland", "Annapolis", "Baltimore oriole"),
    ("Massachusetts", "Boston", "Black-capped chickadee"),
    ("Michigan", "Lansing", "American robin"),
    ("Minnesota", "Saint Paul", "Common loon"),
    ("Mississippi", "Jackson", "Northern mockingbird"),
    ("Missouri", "Jefferson City", "Eastern bluebird"),
    ("Montana", "Helena", "Western meadowlark"),
    ("Nebraska", "Lincoln", "Western meadowlark"),
    ("Nevada", "Carson City", "Mountain bluebird"),
    ("New Hampshire", "Concord", "Purple finch"),
    ("New Jersey", "Trenton", "Eastern goldfinch"),
    ("New Mexico", "Santa Fe", "Greater roadrunner"),
    ("New York", "Albany", "Eastern bluebird"),
    ("North Carolina", "Raleigh", "Northern cardinal"),
    ("North Dakota", "Bismarck", "Western meadowlark"),
    ("Ohio", "Columbus", "Northern cardinal"),
    ("Oklahoma", "Oklahoma City", "Scissor-tailed flycatcher"),
    ("Oregon", "Salem", "Western meadowlark"),
    ("Pennsylvania", "Harrisburg", "Ruffed grouse"),
    ("Rhode Island", "Providence", "Rhode Island Red"),
    ("South Carolina", "Columbia", "Carolina wren"),
    ("South Dakota", "Pierre", "Ring-necked pheasant"),
    ("Tennessee", "Nashville", "Northern mockingbird"),
    ("Texas", "Austin", "Northern mockingbird"),
    ("Utah", "Salt Lake City", "California gull"),
    ("Vermont", "Montpelier", "Hermit thrush"),
    ("Virginia", "Richmond", "Northern cardinal"),
    ("Washington", "Olympia", "American goldfinch"),
    ("West Virginia", "Charleston", "Northern cardinal"),
    ("Wisconsin", "Madison", "American robin"),
    ("Wyoming", "Cheyenne", "Western meadowlark"),
)

# 💡 Lists can change after creation; tuples cannot.
months = ["Jan", "Feb"]
print(len(months))
print(len(days_of_week))

# ⚠️ This raises an error because tuples do not have an append method.
try:
    days_of_week.append("Beatleday")
except AttributeError as error:
    print(f"Tuple error: {error}")

months.append("Mar")
print(months)

# 🔁 Reassigning a name is different from changing a tuple.
SALES_TAX = 0.02
print(f"Sales tax: {SALES_TAX}")

# 🔒 Tuples are immutable, so their items cannot be changed after creation.
# 🔎 Parallel tuples use one index: states[12] and state_capitals[12]
# refer to the same row because the data is kept in matching positions.
# 🔎 Nested tuples use two indexes: [row][column].
# For example, states_and_capitals[12][1] is Illinois's capital.
location = states.index("Illinois")
print(location)

# 🖨️ The row index finds Illinois; columns 0 and 1 select its state and capital.
print(
    f"State:  {states_and_capitals[location][0]},  Capital:  {states_and_capitals[location][1]}"
)
