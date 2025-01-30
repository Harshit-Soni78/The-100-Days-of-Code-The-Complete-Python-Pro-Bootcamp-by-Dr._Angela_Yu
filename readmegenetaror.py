import os

def create_readme_in_folders():
    current_directory = os.getcwd()
    
    for root, dirs, files in os.walk(current_directory):
        for dir_name in dirs:
            readme_path = os.path.join(root, dir_name, 'README.md')
            if not os.path.exists(readme_path):
                with open(readme_path, 'w') as readme_file:
                    readme_file.write(f'# {dir_name}\n\nThis is the README file for the {dir_name} directory.')
                print(f'Created README.md in {os.path.join(root, dir_name)}')

if __name__ == "__main__":
    create_readme_in_folders()