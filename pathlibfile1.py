from pathlib import Path
a=Path("Salam")                     # File is created
a.mkdir(exist_ok=True)

file = a / "Training"                   # File is writed
file.write_text("It made by pathlib")

for word in a.iterdir():                # File is printed
    print(" ", word.name)

file.unlink()                       # File is removed
a.rmdir()