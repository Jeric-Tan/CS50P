from fpdf import FPDF

class Shirt(FPDF):
    def gen(self, txt):
        self.add_page()
        self.set_font('helvetica', 'B', 50)
        self.cell(0, 50, 'CS50 Shirtificate',new_x="LMARGIN", new_y="NEXT", align="C")

        self.image('shirtificate.png', w=pdf.epw)
        self.set_font("helvetica", "B", 35)
        self.set_text_color(255,255,255)
        self.text(55, 115, txt)


        self.output("shirtificate.pdf")

name = input('Name: ')
txt = name.title().strip() + ' took CS50'
pdf = Shirt()
pdf.gen(txt)
