import os
import subprocess

# Define paths
script_name = "forti.py"  # Script name
binary_name = "forti"    # Binary name
destination_path = f"/usr/local/bin/{binary_name}"
man_page_path = "/usr/share/man/man1/fc.1"

def compile_script(script_name):
    try:
        print("Compiling script...")
        subprocess.check_call(["pyinstaller", "--onefile", script_name])
        print("Compilation complete.")
    except subprocess.CalledProcessError as e:
        print(f"Error during compilation: {e}")
        exit(1)

def install():
    try:
        print("Installing related dependencies...")
        subprocess.check_call(["pip", "install", "-r", "requirements.txt"])
        print("Installation complete.")
    except subprocess.CalledProcessError as e:
        print(f"Error during the installation: {e}")

def move_binary():
    # Find the compiled binary in the dist directory
    compiled_binary = f"dist/{binary_name}"
    if os.path.exists(compiled_binary):
        try:
            print("Moving binary to /usr/local/bin...")
            subprocess.check_call(["sudo", "mv", compiled_binary, destination_path])
            print(f"Binary moved to {destination_path}")
        except subprocess.CalledProcessError as e:
            print(f"Error moving binary: {e}")
            exit(1)
    else:
        print(f"Compiled binary not found at {compiled_binary}.")
        exit(1)

def set_permissions():
    try:
        print("Setting permissions...")
        subprocess.check_call(["sudo", "chmod", "+x", destination_path])
        print("Permissions set.")
    except subprocess.CalledProcessError as e:
        print(f"Error setting permissions: {e}")
        exit(1)

def create_man_page():
    man_page_content = """
.TH FC 1 "SEPTEMBER 2024" "VERSION 1.0" "SECURE VICTIM DATABASE TOOL"
.SH NAME
fc \- A powerful and victim data base encryption tool.
.SH SYNOPSIS
fc [options]
.SH DESCRIPTION
fc is a secure tool designed for encrypting and decrypting victim data lists...
    """
    
    try:
        print("Creating man page...")
        # Write man page content to a temporary file
        temp_man_page_path = "/tmp/fc.1"
        with open(temp_man_page_path, 'w') as man_page_file:
            man_page_file.write(man_page_content)
        
        # Move the temporary file to the correct location with sudo
        subprocess.check_call(["sudo", "mv", temp_man_page_path, man_page_path])
        subprocess.check_call(["sudo", "mandb"])
        print("Man page created.")
    except Exception as e:
        print(f"Error creating man page: {e}")

if __name__ == "__main__":
    install()
    compile_script(script_name)
    move_binary()
    set_permissions()
    create_man_page()
