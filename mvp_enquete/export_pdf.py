from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "Rapport d'Affaire", align="C", ln=True)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

def generer_pdf(affaires):
    pdf = PDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    for affaire in affaires:
        pdf.cell(0, 10, str(affaire), ln=True)

    pdf.output("rapport_affaires.pdf")
