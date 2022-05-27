import imp
import shutil
from pathlib import Path

source=Path("compass.png")
target=Path("compass_copy.png")

shutil.copy(source,target)
