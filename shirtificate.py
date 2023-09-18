from fpdf import FPDF   # import de library de pdf

class PDF:
    def __init__(self, name):
        self._pdf = FPDF() # inicialização de um objeto FPDF na propriedade _pdf
        self._pdf.add_page() # uso do método add_page de FPDF para adicionar página à propriedade _pdf
        self._pdf.set_font("helvetica", "B", 50) #método set_fonte
        self._pdf.cell(0, 60, "CS50 Shirtificate", new_x="LMARGIN", new_y="NEXT", align="C") # método cell para adicionar título
        self._pdf.image("shirtificate.png", w=self._pdf.epw) # método image para adicionar imagem ao pdf
        self._pdf.set_font_size(30) # método set_font_size para escolher font para escrever
        self._pdf.set_text_color(255, 255, 255) #método text_color
        self._pdf.text(x=50, y=140, txt=f"{name} took CS50") #escrever texto em algures no pdf (em cima da imagem)

    def save(self, name): #criação de método save para a class PDF
        self._pdf.output(name) #utilização de método output da libraria FPDF para criar um ficheiro pdf com o nome
                                #introduzido. Este método save é aplicado sobre a propriedade _pdf


name = input("Name: ") #ask user for his name
pdf = PDF(name) # vamos criar um objecto da class PDF, cujo argumento é o nome do user
pdf.save("shirtificate.pdf") #vamos chamar o método save da class PDF no objecto pdf e passar o atributo