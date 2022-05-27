from pathlib import Path

test_path=Path("zartab")

if test_path.exists():
    print("Directory already exists")
    test_path.rmdir()
    print("Directory removed")
else:
    test_path.mkdir()

path=Path("../ecommerce")

print(path.iterdir())

for p in path.iterdir():
    print(p)

print("---------------------------------")

# expression for item in items
files=[p for p in path.iterdir()]

print(files)
print("---------------------------------")
directories=[p for p in path.iterdir() if p.is_dir()]
print(directories)
