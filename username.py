import pandas as pd

# Load your CSV file
file_path = "main_spotify.csv"  # Change to the actual file path
df = pd.read_csv(file_path)

# Ensure 'user_id' column exists
if "user_id" not in df.columns:
    raise ValueError("The dataset does not contain a 'user_id' column.")

# Your provided names
provided_names = [
    "bimo", "afrin", "om", "parshuram", "ashish", "aman", "dheeraj", "dhiraj", "akansha", "smita",
    "archana", "archu", "soumya", "arushi", "nikesh", "ashish", "gaurav", "anisha", "vanshika",
    "aditya", "tulsi", "divyaraj", "sneha", "neha", "aruhi", "arpit", "arpita", "amrit", "amrita",
    "mamta", "manju", "navjit", "ramesh", "suresh", "naresh", "niraj", "pankaj", "kanchan", "uttam",
    "ravi", "rakesh", "munna", "pawan", "palak", "nikita", "anjali", "riya", "tannu", "priya",
    "ishu", "ishika", "achyuttam", "jyoti", "annu", "anup", "anuj", "ashirwad", "upmanyu", "abhishek",
    "ankur", "samay", "ajay", "arvind", "rajesh", "dipanshu", "divyansh", "sagar", "mohit", "nikunj",
    "nishil", "milind", "vinit", "khushi", "shalini", "shruti", "ambika", "juhi", "kavita", "renuka",
    "pooja", "maahi", "ritu", "ashma", "madhu", "palak", "diksha", "nidhi", "chanchal", "pinki",
    "pinky", "piyush", "akshara", "prisha", "tisha", "pratibha", "priyanka", "somnath", "adarsh",
    "kalua", "goblin", "Bimochan", "himanshu", "shivam", "kuldeep", "kusum", "suman", "sejal",
    "harsh", "harshit", "vikas", "vishal", "vaishali", "anamika", "megha", "savan", "abhi", "amit",
    "deepak", "hitesh", "sashi", "shubham", "shrikant", "nilesh", "nikesh", "aman", "anand",
    "happy", "farheen", "pushpita", "jyotsna", "kajal", "vaishnavi", "monika", "varsha", "parvati",
    "soni", "sonali", "anuv", "arijit", "sonu", "udit", "raghav", "samir", "jahangeer", "tirath",
    "nitin", "basant", "suraj", "ranjan", "kalpesh", "bunty", "yash", "ankush", "asha", "urmii",
    "nihit", "ayush", "akshay", "akhilesh", "aryan", "nishant", "nikita", "akash", "ridhi",
    "sudhanshu", "vartika", "sundar", "raj", "saurabh", "vishant", "deepanshu", "vivek", "teerath",
    "priyanshi", "priyanshu", "alok", "mukesh", "rashmi", "anubhav", "sarthika", "rahul",
    "shashank", "anurag"
]

# Find unique user_ids in the dataset
unique_user_ids = df["user_id"].unique()

# Generate additional names if required
import random

while len(provided_names) < len(unique_user_ids):
    provided_names.append("User" + str(random.randint(1000, 9999)))  # Generate random usernames

# Shuffle names to distribute them randomly
random.shuffle(provided_names)

# Create a mapping of user_id to username
user_mapping = {user_id: name for user_id, name in zip(unique_user_ids, provided_names)}

# Add the username column
df["username"] = df["user_id"].map(user_mapping)

# Save the updated file
updated_file_path = "main_spotifyy.csv"  # Change this to your desired path
df.to_csv(updated_file_path, index=False)

print(f"Updated file saved as: {updated_file_path}")
