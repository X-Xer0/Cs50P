from fpdf import FPDF

class Shirtificate(FPDF):
    def header(self):
        self.set_font("Arial", "B", 24)
        self.cell(0, 10, "CS50 Shirtificate", ln=True, align="C")
        self.ln(20)

def create_shirtificate(name):
    pdf = Shirtificate(orientation="P", format="A4")
    pdf.add_page()
    pdf.image("shirtificate.png", x=0, y=60, w=210)
    pdf.set_font("Arial", "B", 36)
    pdf.set_text_color(255, 255, 255)
    pdf.text(x=55, y=150, txt=f"{name} took CS50!")
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    name = input("Name: ")
    create_shirtificate(name)
