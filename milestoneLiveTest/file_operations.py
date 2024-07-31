def read_file(file_path):
    """
    Reads the content of a file and returns it as a string.
    
    :param file_path: Path to the file to be read
    :return: Content of the file as a string
    """
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")

def write_file(file_path, data):
    """
    Writes data to a file, overwriting any existing content.
    
    :param file_path: Path to the file to be written to
    :param data: Data to be written to the file
    """
    try:
        with open(file_path, 'w') as file:
            file.write(data)
        print(f"Data successfully written to {file_path}")
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")

def append_file(file_path, data):
    """
    Appends data to a file.
    
    :param file_path: Path to the file to be appended to
    :param data: Data to be appended to the file
    """
    try:
        with open(file_path, 'a') as file:
            file.write(data)
        print(f"Data successfully appended to {file_path}")
    except Exception as e:
        print(f"An error occurred while appending to the file: {e}")

# Example usage:
if __name__ == "__main__":
    file_path = "example.txt"
    
    # Writing to a file
    write_file(file_path, "Hello, world!\n")
    
    # Appending to a file
    append_file(file_path, "This is an appended line.\n")
    
    # Reading from a file
    content = read_file(file_path)
    print("File content:")
    print(content)

