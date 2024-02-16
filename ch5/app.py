import json
# Reading Files

# key:
# file path (relative thd python app)
# mode
f = open("./ch5/example.json")
data = json.loads(f.read())
print(data[0]["name"])
f.close()

f = open("./ch5/example.csv")
for dat in f.readlines():
    print(dat)
f.close()

# Writing Files
with open("./ch5/test.txt", "w", encoding="utf-8") as f:
    f.write("my first file\n")
    f.write("This file\n\n")
    f.write("contains three lines\n")
    f.close()
f = open("./ch5/test.txt", "a", encoding="utf-8")
f.write("this is appending processs\n")
f.close()

# Challenge
# buat program untuk membaca dan mengupdate
# file JSON

fj = open("./ch5/example.json", "r", encoding="utf-8")
dat = json.loads(fj.read())
dat.append(
    {
        "name": "test2",
        "age": "12",
    }
)
fj.close()
fj = open("./ch5/example.json", "w", encoding="utf-8")
fj.write(json.dumps(dat))
fj.close()

# Error handler
try:
    print(x)
except:
    print("An exception occurred")
finally:
    print("enter finally block")


fj = open("./ch5/example1.json", "w", encoding="utf-8")
try:
    dat = json.loads(fj.read())
    dat.append(
        {
            "name": "test2",
            "age": "12",
        }
    )
    fj.write(dat)
    raise Exception("invalid data format")
except NameError:
    print("failed to write example1.json file")
except BufferError:
    print("")
finally:
    fj.close()

print({"a": "this is a", "b": "this is b"})
