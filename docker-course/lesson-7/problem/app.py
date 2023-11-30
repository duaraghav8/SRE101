import os
from datetime import datetime

data_file = "/data/data.txt"


# Try to read the data file
# If file already exists, just print its data on screen
# If it does not exist, create it and populate it with message
def main():
    if os.path.isfile(data_file):
        print(f"FILE {data_file} ALREADY EXISTS!")
        print("Printing contents ->\n")

        with open(data_file, "r") as reader:
            print(reader.read())
            print()
    else:
        print(f"FILE {data_file} DOESN'T ALREADY EXIST")

        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        message = f"Hello world!\nThis message was written on {now}"
        print(f"Creating new file with message ->\n\n{message}\n")

        with open(data_file, "w") as writer:
            writer.write(message)

        print("Done!")
    
    input("Press ENTER to exit")


if __name__ == "__main__":
    main()
