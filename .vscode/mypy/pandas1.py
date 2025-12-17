import pandas as pd
#pd.set_option('display.max_rows', None)        # Show all rows
pd.set_option('display.max_columns', None)     # Show all columns
#pd.set_option('display.width', None)           # Unlimited width
pd.set_option('display.max_colwidth', None)    # Show full text in each cell
#df=pd.DataFrame([[1,2,3],[4,5,6],[7,8,6]],columns=["A","B","C"],index=["X","Y","Z"])
#print(df.head())  RETURNS FIRST 5 ROWS    VALUE CAN BE WRITTEN INSIDE PARENTHESIS TO SPECIFY NUMBER OF ROWS
#df.tail()    simlarly
#rows are called index and columns same
#print(df.columns)
#print(df.index)
#print(df.info())
#print(df.describe())
#print(df.shape)
#print(df.nunique())    number of unique elements in each column
#coffee = pd.read_csv("C:/Users/Pratham/c++/.vscode/coffee.csv")
#coffee = pd.read_csv("coffee.csv")
#print(coffee.head())
#import pandas as pd
#import pandas as pd
import random

# Sample data lists
names = [
    "Aarav", "Vivaan", "Aditya", "Vihaan", "Arjun", "Sai", "Reyansh", "Krishna", "Ishaan", "Kabir",
    "Ananya", "Diya", "Isha", "Mira", "Saanvi", "Riya", "Aadhya", "Anika", "Sara", "Myra",
    "Rahul", "Rohan", "Kunal", "Yash", "Samarth", "Rehan", "Harsh", "Om", "Atharv", "Tejas",
    "Priya", "Kritika", "Pooja", "Shreya", "Tanvi", "Avni", "Nisha", "Meera", "Kashish", "Simran",
    "Arnav", "Dev", "Manav", "Nikhil", "Siddharth", "Daksh", "Rudra", "Shaurya", "Viraj", "Aryan"
]

sports = ["Cricket", "Football", "Basketball", "Hockey", "Badminton", "Tennis", "Volleyball"]

# Generate heights between 150 cm and 190 cm
heights = [random.randint(150, 190) for _ in range(50)]

# Randomly assign sports
assigned_sports = [random.choice(sports) for _ in range(50)]

# Create DataFrame
df = pd.DataFrame({
    "Name": names,               # 50 names are already listed
    "Height (cm)": heights,
    "Sport": assigned_sports
})

# Save to Excel file
df.to_excel("candidates.xlsx", index=False)

#print("Excel file 'candidates.xlsx' created successfully!")

coffee = pd.read_csv(".vscode/mypy/coffee.csv")

df = pd.read_excel(r"C:\Users\Pratham\Downloads\Olympic Athletes.xlsx")
print(df.head())

df = pd.read_excel("candidates.xlsx")
#print(df[df['Name'].str.contains("a",case=False)])
#print(df)
#print(df[(df["Height (cm)"]>169) & (df.index>25)])
#print(coffee)
#print(coffee.loc[:,[0,1,2]])     in loc rows and columns are treated differently
#print(coffee.iloc[:,[0,1,2]])    in iloc both r and c are treated with numbers
#the csv file can be edited as well
#coffee.loc[:,"Value"]=coffee.loc[:,"Value"]+1   doesnt change value in actual file but memory
#print(coffee)
#print(coffee.sort_values(["Value","Name"],ascending=[0,1]))
#print(coffee)
#for index,row in coffee.iterrows():
    #print(index)
    #print(row)
    #print("\n")







