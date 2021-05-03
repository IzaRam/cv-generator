from reportlab.lib.pagesizes import A4
from reportlab.pdfgen.canvas import Canvas

def drawMyRuler(pdf):
    pdf.setFillColorRGB(255,0,0)
    pdf.drawString(100,810, 'x100')
    pdf.drawString(200,810, 'x200')
    pdf.drawString(300,810, 'x300')
    pdf.drawString(400,810, 'x400')
    pdf.drawString(500,810, 'x500')

    pdf.drawString(10,100, 'y100')
    pdf.drawString(10,200, 'y200')
    pdf.drawString(10,300, 'y300')
    pdf.drawString(10,400, 'y400')
    pdf.drawString(10,500, 'y500')
    pdf.drawString(10,600, 'y600')
    pdf.drawString(10,700, 'y700')
    pdf.drawString(10,800, 'y800')

pdf = Canvas('cv.pdf', pagesize=A4)

pdf.setTitle("My CV")

name = "First Last"
pdf.setFont("Times-Bold", 16)
pdf.drawString(30, 810, name)

## Educação
pdf.setFont("Times-Bold", 12)
pdf.drawString(30, 780, "Educação")
pdf.line(30, 775, 550, 775)


instituicao = "Universidade Nome"
pdf.setFont("Times-Bold", 11)
pdf.drawString(30, 760, instituicao)

curso = "Curso Nome"
pdf.setFont("Times-Roman", 11)
pdf.drawString(250, 760, curso)

data = "Março 2015 - Outubro 2020"
print(len(data))
pdf.setFont("Times-Bold", 11)
pdf.drawString(415, 760, data)
pdf.drawString(545, 760, '*')

t = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc malesuada eu turpis quis auctor. Nullam non "
print(len(t))

extra1 = [u'\u2022   ' + "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc malesuada eu turpis quis auctor. "
                         "Nullam non ",
          "     sodales metus. Praesent tristique tempus lorem, et luctus eros venenatis quis. "]
pdf.setFont("Times-Roman", 11)
text = pdf.beginText(45, 745)
for line in extra1:
    text.textLine(line)
pdf.drawText(text)

extra2 = [u'\u2022   ' + "Nulla facilisi. Curabitur in libero magna. "]
text = pdf.beginText(45, 715)
for line in extra2:
    text.textLine(line)
pdf.drawText(text)


# Trabalhos
pdf.setFont("Times-Bold", 12)
pdf.drawString(30, 690, "Experiência Profissional")
pdf.line(30, 685, 550, 685)

posicao = "Posição Nome"
pdf.setFont("Times-Bold", 11)
pdf.drawString(30, 670, posicao)

empresa = "Empresa Nome"
pdf.setFont("Times-Roman", 11)
pdf.drawString(250, 670, empresa)

data = "Agosto 2015 - Maio 2020"
print(len(data))
pdf.setFont("Times-Bold", 11)
pdf.drawString(430, 670, data)
pdf.drawString(545, 670, '*')

extra1 = [u'\u2022   ' + "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc malesuada eu turpis quis auctor. "
                         "Nullam non ",
          "     sodales metus. Praesent tristique tempus lorem, et luctus eros venenatis quis. "]
pdf.setFont("Times-Roman", 11)
text = pdf.beginText(45, 655)
for line in extra1:
    text.textLine(line)
pdf.drawText(text)

extra2 = [u'\u2022   ' + "Nulla facilisi. Curabitur in libero magna. "]
text = pdf.beginText(45, 625)
for line in extra2:
    text.textLine(line)
pdf.drawText(text)


drawMyRuler(pdf)

pdf.drawString(0, 0, "Origin")

pdf.save()
