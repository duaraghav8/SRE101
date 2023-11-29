import os

data_file = "/data/data.txt"
message = "Hello world!"


# Try to read the data file
# If file already exists, just print its data on screen
# If it does not exist, create it and populate it with message
def main():
    if os.path.isfile(data_file):
        print(f"FILE {data_file} ALREADY EXISTS!")
        print("Printing contents...")

        with open(data_file, "r") as reader:
            print(reader.read())
    else:
        print(f"FILE {data_file} DOESN'T ALREADY EXIST")
        print(f"Creating new file with message message '{message}'")

        with open(data_file, "w") as writer:
            writer.write(message)

        print("Done!")
    
    input("Press ENTER to exit")


if __name__ == "__main__":
    main()
