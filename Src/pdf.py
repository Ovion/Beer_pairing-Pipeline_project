from fpdf import FPDF


def create_pdf (df_estilo, df_cerv, state):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    pdf.multi_cell(0, 10, 'Maridaje y Cervecerías', align='C')
    pdf.ln(10)
    pdf.set_font('Arial', '', 12)
    text="El siguiente dataframe muestra el maridaje del tipo de cerveza:\n{} \n\n Este otro muestra las cervecerías en {}: \n{}"

    pdf.multi_cell(0, 5, text.format(df_estilo, state, df_cerv), align='L')
    pdf.ln(10)

    pdf.output('../Outputs/atun.pdf', 'F')



