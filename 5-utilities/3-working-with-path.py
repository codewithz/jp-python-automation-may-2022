from pathlib import Path 

path1=Path(r"D:\Zartab\Trainings")
print(path1)

current_path=Path()
print("Current Path:",current_path)

path2=Path("../ecommerce/__init__.py")
print(path2)

combined_path=Path()/Path("test")
print(combined_path)

print("Exists",path2.exists())
print("Exists", combined_path.exists())
print("Is File",path2.is_file())
print("Is Dir",path2.is_dir())

print("Name:",path2.name)
print("Stem:",path2.stem)
print("Suffix:",path2.suffix)
print("Parent:",path2.parent)
print("Absolute:",path2.absolute())
