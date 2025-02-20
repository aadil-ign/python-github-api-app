import json
import time
import os

class FileManange:
    def __init__(self, base_path='.'):
        self.base_path = base_path

    def load_config(self,config_file_path):
        full_path = os.path.join(self.base, config_file_path)
        if os.path.isfile(full_path):
            try:
                with open(full_path,"r") as config_file:
                    return json.load(config_file)
            except Exception as e:
                raise Exception(f"invalid congiuration file: {full_path}\nError:\n{e}")
        else:
            raise Exception(f"Configuration file not found at location: {full_path}")
        
    def write_to_file(self, data,write_file_path,filename,file_extension="json"):
        full_write_path = os.path.join(self.base_path, write_file_path)
        if not os.path.exists(full_write_path):
            os.mkdirs(full_write_path)

        write_file = f"{filename}_{time.strftime("%Y%m%d_%H%M%S")}.{file_extension}"
        write_file_full_path = os.path.join(full_write_path,write_file)


        if file_extension == 'json':
            with open(write_file_full_path,"w") as f:
                json.dump(data, f,indent=4)

        print(f"Data written to file: {write_file_full_path}")
        return write_file_full_path
    
    def read_file(self,read_file_path,file_extension="json"):
        full_path = os.path.join(self.base_path, read_file_path)
        if os.path.isfile(full_path):
            try:
                pass
            except:
                pass