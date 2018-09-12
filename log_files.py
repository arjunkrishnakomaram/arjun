file_name = r"C:\Users\Admin\Desktop\New folder\access_log_Jul95_new.txt"

output = []

pattern = ["jarceo.extern.ucsd.edu"]

with open(file_name, 'r', errors='ignore') as f:
    s = f.readlines()
for line_no, line in enumerate(s,1):
    for data in pattern:
        if data in line:
            output.append(line)
            print('url is present in this line : ', line_no)
            break

print("No.of times URL accessed is : ", output)
for ele in output:
    print(ele)
print('the length of the output is :  ', len(output))
