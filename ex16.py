from sys import argv

script, filename = argv

print(f"we're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^).")
print("if you do want that, hit RETURN")

input("?")

print("opening the file...")
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
target.truncate()

print("now i'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("i'm going to write these to the file.")

#txt_to_write = line1 + ("\n") + line2 + ("\n") + line3 + ("\n")
#target.write(txt_to_write)

txt_to_write = "{}\n{}\n{}\n"
target.write(txt_to_write.format(line1,line2,line3))

#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

print("And finally, we close it.")
target.close()
