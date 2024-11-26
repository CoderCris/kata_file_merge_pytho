import os


def get_project_path():
    try:
        path = input("INPUT :: Absolute PATH to project:")
        if not os.path.isdir(path):
            raise FileNotFoundError(f"The directory '{path}' does not exist.")
        if not os.access(path, os.R_OK):
            raise PermissionError(f"The script does not have read permissions for '{path}'.")
        
        return path
    
    except FileNotFoundError as e:
        print(f"ERROR :: {e}")
        return None

    except PermissionError as e:
        print(f"ERROR :: {e}")
        return None

def get_relevant_files_path(project_path):
    directories_to_search = [project_path, os.path.join(project_path, 'src')]
    listed_files = []
    for directory in directories_to_search:
        for root, _, files in os.walk(directory):
            for file in files:
                if not os.path.isfile(file):
                    listed_files.append(os.path.join(root, file))

    
    
    return listed_files

def print_files(file_paths):
    for file_path in file_paths:
        print (file_path)

def merge_files(file_paths, output_file):
    try:
        with open(output_file, 'w', encoding='utf-8') as output:
            for file_path in file_paths:
                try:
                    # Add a tag indicating the start of a file
                    file_name = os.path.basename(file_path)
                    output.write(f"===== START OF FILE: {file_name} =====\n")
                    
                    # Read the content of the file and write it to the output
                    with open(file_path, 'r', encoding='utf-8') as input_file:
                        content = input_file.read()
                        output.write(content)
                    
                    # Add a tag indicating the end of a file
                    output.write(f"\n===== END OF FILE: {file_name} =====\n\n")
                
                except Exception as e:
                    print(f"Error reading file '{file_path}': {e}")
    
        print(f"Files have been successfully merged into '{output_file}'.")
    
    except Exception as e:
        print(f"Error creating the output file '{output_file}': {e}")

def main():
    print("INIT :: Script ")
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    output_file = input("INPUT :: Output file name --> ")
    project_path = get_project_path()
    file_paths = get_relevant_files_path(project_path)
    output_file_path = os.path.join(desktop_path, output_file)
    merge_files(file_paths, output_file_path)
    print(project_path)
    return None 

if __name__ == '__main__': 
    main()