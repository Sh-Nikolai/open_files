import os

files_len = {}

for filename in os.listdir('files'):
    files_len[filename] = []
    # print(filename)
    with open(os.path.join('files', filename), 'r', encoding='utf-8') as f:
        text = f.readlines()

        # print(text)

        count = 0
        for line in text:
            # print(line)
            count = count + 1
        # files_len[filename] = count
        files_len[filename].append(count)
        files_len[filename].append(text)

# print(files_len)

result = []
with open ('resalt_file.txt', 'w', encoding='UTF-8') as result:
    for k, v in sorted (files_len.items(), key = lambda para:(para[1])):
        result.write(k + '\n')
        result.write(str(v[0])+'\n')
        result.write(','.join(v[1]) + '\n')





# print(result)d
# result = list(result)
# print(result)
# with open(os.path.join('files', filename), 'r', encoding='utf-8') as f:
#     text = f.readlines()
#     for i in result:
#         result.append(text)
#
# print(result)





