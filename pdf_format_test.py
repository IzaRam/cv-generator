from reportlab.lib.pagesizes import A4
from reportlab.pdfgen.canvas import Canvas


def get_content_personal():
    name = input("Digite seu nome: ")
    email = input("Digite seu email: ")
    numero = input("Digite seu numero: ")
    all_content = {
        'name': name,
        'email': email,
        'numero': numero
    }
    return all_content


def get_content_edu():
    uni = input("Digite sua universidade: ")
    curso = input("Digite seu curso: ")
    data = input("Digite a data: ")
    infos = []
    while (True):
        q = int(input("Digite 1 para adicionar infos: "))
        if q == 1:
            extra = input("Digite extras: ")
            infos.append(extra)
        else:
            break
    all_content = {
        'name': name,
        'uni': uni,
        'curso': curso,
        'data': data,
        'infos': infos
    }
    return all_content


def get_content_pro():
    cargo = input("Digite seu cargo: ")
    comp = input("Digite sua empresa: ")
    data = input("Digite a data: ")
    infos = []
    while (True):
        q = int(input("Digite 1 para adicionar infos: "))
        if q == 1:
            extra = input("Digite extras: ")
            infos.append(extra)
        else:
            break
    all_content = {
        'pos': cargo,
        'emp': comp,
        'data': data,
        'infos': infos
    }
    return all_content


def get_extras(infos):
    extras = []
    for extra in infos:
        if len(extra) > 106:
            list_words = extra.split(" ")
            list_lines = []
            str = u'\u2022   '
            for i in range(len(list_words)):
                if len(str) + len(list_words[i]) < 106:
                    str += " " + list_words[i]
                else:
                    list_lines.append(str)
                    str = "     " + list_words[i]

                if i == len(list_words) - 1:
                    list_lines.append(str)

            extras.append(list_lines)
        else:
            extras.append([u'\u2022   ' + extra])
    return extras


# Create PDF
pdf = Canvas('cv_test.pdf', pagesize=A4)
pdf.setTitle("My CV")


# Informações Pessoais
cont_personal = get_content_personal()

name = cont_personal['name']
pdf.setFont("Times-Bold", 16)
pdf.drawString(30, 810, name)

email = cont_personal['email']
pos_x = 545 - len(email) * 5
pdf.setFont("Times-Roman", 11)
pdf.drawString(pos_x, 815, email)

numero = cont_personal['numero']
pos_x = 545 - len(numero) * 5
pdf.setFont("Times-Roman", 11)
pdf.drawString(pos_x, 800, numero)

pos_y_total = 0


# Educação
cont = get_content_edu()

pdf.setFont("Times-Bold", 12)
pdf.drawString(30, 780, "Educação")
pdf.line(30, 775, 550, 775)

pos_y_total += 5

instituicao = cont['uni']
pdf.setFont("Times-Bold", 11)
pdf.drawString(30, 760, instituicao)

pos_y_total += 15

curso = cont['curso']
pdf.setFont("Times-Roman", 11)
pdf.drawString(250, 760, curso)

data = cont['data']
pos_x = 545 - len(data) * 5
pdf.setFont("Times-Bold", 11)
pdf.drawString(pos_x, 760, data)

pos_y_total += 15

pos_y = 745
extras = get_extras(cont['infos'])
for extra in extras:
    print(extra)
    pdf.setFont("Times-Roman", 11)
    text = pdf.beginText(45, pos_y)
    for line in extra:
        text.textLine(line)
        pos_y -= 15
        pos_y_total += 15
    pdf.drawText(text)


# Trabalhos
cont_pro = get_content_pro()

pos_y = 780 - pos_y_total
pdf.setFont("Times-Bold", 12)
pdf.drawString(30, pos_y, "Experiência Profissional")
pdf.line(30, pos_y - 5, 550, pos_y - 5)

pos_y_total += 20

pos_y = 780 - pos_y_total
posicao = cont_pro['pos']
pdf.setFont("Times-Bold", 11)
pdf.drawString(30, pos_y, posicao)

empresa = cont_pro['emp']
pdf.setFont("Times-Roman", 11)
pdf.drawString(250, pos_y, empresa)

data = cont_pro['data']
pos_x = 545 - len(data) * 5
pdf.setFont("Times-Bold", 11)
pdf.drawString(pos_x, pos_y, data)

pos_y_total += 15

pos_y = 780 - pos_y_total
extras = get_extras(cont_pro['infos'])
for extra in extras:
    print(extra)
    pdf.setFont("Times-Roman", 11)
    text = pdf.beginText(45, pos_y)
    for line in extra:
        text.textLine(line)
        pos_y -= 15
        pos_y_total += 15
    pdf.drawText(text)


# Save PDF
pdf.save()
