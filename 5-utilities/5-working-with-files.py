from pathlib import Path
from time import ctime

path=Path("company.txt")
print("Stats",path.stat())

print("Creation Time",ctime(path.stat().st_ctime))

#Reading from File 

data_from_file=path.read_text()
print("-------------------Data from FIle----------")

print(data_from_file)

print(40*'-')

#Write to File 
print("-------------------Writing to FIle----------")
path_to_write=Path("some_data.txt")
path_to_write.write_text(data_from_file)
print("Done")

print(40*'-')