def get_string():
    infos = []
    while (True):
        q = int(input("Digite 1 para adicionar infos: "))
        if q == 1:
            extra = input("Digite extras: ")
            infos.append(extra)
        else:
            break
    return infos


inf = get_string()

extras = []
for extra in inf:
    if len(extra) > 106:
        list_words = extra.split(" ")
        list_lines = []
        str = ""
        # for word in list_words:
        for i in range(len(list_words)):
            if len(str) + len(list_words[i]) < 106:
                str += " " + list_words[i]
            else:
                list_lines.append(str)
                str = "" + list_words[i]

            if i == len(list_words)-1:
                list_lines.append(str)

        extras.append(list_lines)
    else:
        extras.append([extra])

print(extras)