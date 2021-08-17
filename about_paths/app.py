from pathlib import Path

un = Path()
deux = Path("about")

# relative path
print(un)
# absolute path
print(un.absolute())
# check for existence of path
print(deux.absolute())
print(deux.exists())
# path does not exist; create it
# deux.mkdir()
# delete path
# deux.rmdir()
# list out the entire content of a directory
for file in un.glob("*"):
    print(file)
