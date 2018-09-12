file_name1 = r"C:\Users\Admin\Desktop\New folder\access_log_Jul95_new.txt"

pattern = "14/Jul/1995"
empty= []
fop = open(file_name1,'r',errors='ignore')
reading_file = fop.readlines()
fop.close()
for data in reading_file:
    for date in pattern:
        if date in data:
            empty.append(data)
            break
print(empty)
