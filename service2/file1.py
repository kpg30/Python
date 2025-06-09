import os
from pathlib import Path
from default_logger import Logger

logger = Logger.get_logger("file1")

class FileTest:
    
    @staticmethod
    def read_file(filename : str):
        try:
            # open and read a file
            with open(filename, "r") as file:
                read_data = file.read()
            logger.info(read_data)
            file.close()
        except FileNotFoundError as Error:
            logger.error(f"Error while opening file, {Error}.")
            raise Error
        
    @staticmethod
    def write_to_file(filename: str):
        try:              
            # Writing to a new file or overwriting an existing one
            with open(filename, "w") as file:
                file.write("This is the first line.\n")
                file.write("This is the second line.\n")
                
            logger.info(file)
        except Exception as Error:
            logger.error(f"Error writing to the file, {Error}.")
            raise Error
        
    @staticmethod
    def append_to_file(filename: str):
        try:
            # Appending to an existing file
            with open(filename, "a") as file:
                file.write("This is a new line appended at the end.\n")
                
            logger.info(file)
        except Exception as Error:
            logger.error(f"Error writing to the file, {Error}.")
            raise Error
        
    @staticmethod
    def create_new_file(filename: str):
        try:
            # Appending to an existing file
            with open(filename, "x") as file:
                file.write("This is a new file.\n Hello Prasad. \n")     
            # reading file  
            FileTest.read_file(filename)
        except Exception as Error:
            logger.error(f"Error writing to the file, {Error}.")
            raise Error        
        
def main():
        
    # file_path = r'D:\DataEngineer\Python\Python_Main\service2\test\sample.txt' #'/service2/test'
    file_name = 'sample.txt'
    
    # new file 
    base_name = 'sample'
    counter = "5"
    ext = ".txt"
    new_file = f"{base_name}_{counter}{ext}"
    
    # full_path = f"{file_path}\{file_name}"
    # full_path = os.path.join(file_path, file_name)
    # full_path.replace("\\\\","\\")
    
    #FileTest.create_new_file(new_file)
    FileTest.write_to_file(file_name)
    FileTest.append_to_file(file_name)
    FileTest.read_file(file_name)
    
if __name__ == "__main__":
    main()
    
    
        
        
        
        
    
            
        