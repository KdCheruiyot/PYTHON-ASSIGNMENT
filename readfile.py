def read_and_modify_file():
    filename = input("Enter the filename to read from: ")

    
        with open(filename, 'r') as file:
            content = file.read()
            print("\nOriginal File Content:\n")
            print(content)

            # Modify content (Example: convert to uppercase)
            modified_content = content.upper()

        # Write the modified content to a new file
        new_filename = "modified_" + filename
        with open(new_filename, 'w') as new_file:
            new_file.write(modified_content)
            print(f"\nModified content has been saved to '{new_filename}'")

    except FileNotFoundError:
        print(f"\n Error: The file '{filename}' does not exist.")
    except IOError:
        print("\n Error: Could not read the file or write to the new file.")

# Call the function
read_and_modify_file()
