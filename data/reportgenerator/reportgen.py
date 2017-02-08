# report libs
import time
import platform
from data.libs.reportlab.lib.enums import TA_JUSTIFY, TA_CENTER
from data.libs.reportlab.lib.pagesizes import letter,A4,LEGAL
from data.libs.reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer,Table, TableStyle, Image
from data.libs.reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from data.libs.reportlab.lib.units import inch
from data.libs.reportlab.lib import colors



def dataparser(savelocation, pageformat, margin, paramdata):
    file = logo = address = company = dpto = user = mark = markimg = metadata = ""

    thumbs = thyrdPres = []
    for value in paramdata:
        if "path:" in value:
            file = str(value.replace("path:", ""))
            if platform.system() == 'Windows':
                file = str(file.replace("\\   ", "/"))
        if "logo:" in value:
            logo = str(value.replace("logo:", ""))
            if platform.system() == 'Windows':
                logo = str(logo.replace("\\   ", "/"))
        if "face:" in value:
            mark = str(value.replace("face:", ""))
        if "company:" in value:
            company = str(value.replace("company:", ""))
        if "dpto:" in value:
            dpto = str(value.replace("dpto:", ""))
        if "address:" in value:
            address = str(value.replace("address:", ""))
        if "user:" in value:
            user = str(value.replace("user:", ""))
        if "mark " in value:
            mark = str(value.replace("mark ", ""))
            mark = str(mark.replace("], [", "]\n["))
        if "markimg" in value:
            try:
                markimg = str(value.replace("markimg", ""))
            except:
                pass

        if "thumbs:" in value:
            b =str(value.replace("thumbs:", ""))
            thumbs.append(b)

        if "exif:" in value:
            metadata = str(value.replace("metadata ", ""))

        if "trdp" in value:
            a = str(value.replace("trdp:", ""))
            if "[]" in a:
                a = str(a.replace("[]", ""))
            thyrdPres.append(a)



    configpage = configpg(pageformat)
    repgen(savelocation, configpage, margin, file, logo, company,address, dpto, user, mark, markimg, thumbs,metadata, thyrdPres)


def configpg(pformat):
    if pformat == "letter":
        pformat = letter
    if pformat == "a4":
        pformat = A4
    if pformat == "legal":
        pformat = LEGAL

    return pformat


def repgen(savelocation,pagesize, margin, file, logo, company,address, dpto, user, mark,
           markimg, thumbs, metadata, thyrdPres):



    doc = SimpleDocTemplate(savelocation, pagesize=pagesize,
                            rightMargin=int(margin[0]), leftMargin=int(margin[1]),
                            topMargin=int(margin[2]), bottomMargin=int(margin[3]))
    Story = []
    img1 = Image(logo, 1 * inch, 1 * inch)
    img2 = Image(file)
    img2._restrictSize(4 * inch, 4 * inch)

    if markimg !="":
        markimg = Image(markimg)
        markimg._restrictSize(4 * inch, 4 * inch)

    formatted_time = time.ctime()
    Story.append(img1)


    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))

    ptext = '<font size=12>%s</font>' % company
    Story.append(Paragraph(ptext, styles["Title"]))

    ptext = '<font size=12>%s</font>' % dpto
    Story.append(Paragraph(ptext, styles["Title"]))

    ptext = '<font size=10>%s</font>' % address
    Story.append(Paragraph(ptext, styles["Title"]))
    Story.append(Spacer(1, 12))

    ptext = '<font size=10>%s</font>' % formatted_time
    Story.append(Paragraph(ptext, styles["Normal"]))

    ptext = '<font size=10>Localização do Arquivo analisado: %s</font>' % file
    Story.append(Paragraph(ptext, styles["Normal"]))

    Story.append(img2)
    if mark != "[]":
        text = '<font size=10>marcações realizadas nesse teste: </font>'
        Story.append(Paragraph(text, styles["Normal"]))
        text = '<font size=10>%s</font>' % mark
        Story.append(Paragraph(text, styles["Normal"]))
        Story.append(Spacer(1, 12))
        try:
            Story.append(markimg)
        except:
            pass

    text = '<font size=10><center>Testes realizados:</center></font>'
    Story.append(Paragraph(text, styles["Title"]))

    if metadata != "":
        text = '<font size=10>EXIF/XMP/ICC Profile</font>'
        Story.append(Paragraph(text, styles["Normal"]))
        Story.append(Spacer(1, 12))
        text = '<font size=10>%s</font>' % metadata
        Story.append(Paragraph(text, styles["Normal"]))
        Story.append(Spacer(1, 12))

    try:
        if thyrdPres !=[]:
            for i in thyrdPres:
                if "Illuminant" in i:
                    text = '<font size=10>Illuminant-based Transformed Spaces for Image Forensics</font>'
                    Story.append(Paragraph(text, styles["Normal"]))
                    text = '<font size=10>%s</font>' % i
                    Story.append(Paragraph(text, styles["Normal"]))
                    Story.append(Spacer(1, 12))
    except:
        text = '<font size=10>não foi possivel carregar resultados do illuminants</font>'
        Story.append(Paragraph(text, styles["Normal"]))
        Story.append(Spacer(1, 12))





    try:
        text = '<font size=10>Thumbnail</font>'
        Story.append(Paragraph(text, styles["Normal"]))
        Story.append(Spacer(1, 12))
        for i in thumbs:
            if i is not '':
                if 'thumb' in i:
                    text = '<font size=10>%s</font>' % i
                    Story.append(Paragraph(text, styles["Normal"]))
                    Story.append(Spacer(1, 12))
                    t = Image(i)
                    Story.append(t)
    except:
        text = '<font size=10>Não foi possivel carregar thumbnails</font>'
        Story.append(Paragraph(text, styles["Normal"]))
        Story.append(Spacer(1, 12))

    doc.build(Story)
