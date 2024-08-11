from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image

def create_receipt(transaction_id, date, items, total_amount, customer_name, company_name, logo_path):
    receipt_filename = f"Receipt_{transaction_id}.pdf"
    pdf = SimpleDocTemplate(receipt_filename, pagesize=letter)

    elements = []

    # Add Company Logo and Name
    if logo_path:
        logo = Image(logo_path, 2 * inch, 1 * inch)
        elements.append(logo)
    elements.append(Spacer(1, 12))
    
    styles = getSampleStyleSheet()
    title_style = styles['Title']
    normal_style = styles['Normal']
    
    # Add Company Name as Title
    title = Paragraph(company_name, title_style)
    elements.append(title)

    # Add Receipt Heading
    receipt_heading = Paragraph(f"<b>Transaction Receipt</b>", ParagraphStyle(name="Heading", fontSize=16, spaceAfter=12))
    elements.append(receipt_heading)
    
    # Add Transaction and Customer Details
    transaction_details = [
        ["<b>Transaction ID:</b>", transaction_id],
        ["<b>Date:</b>", date],
        ["<b>Customer Name:</b>", customer_name],
    ]
    
    for detail in transaction_details:
        elements.append(Paragraph(f"{detail[0]} {detail[1]}", normal_style))
    
    elements.append(Spacer(1, 12))
    
    # Add Items Table
    item_data = [["Item", "Quantity", "Unit Price", "Total Price"]]
    for item in items:
        total_price = item['quantity'] * item['price']
        item_data.append([item['name'], item['quantity'], f"${item['price']:.2f}", f"${total_price:.2f}"])

    table = Table(item_data, hAlign='LEFT')
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.darkblue),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.lightblue),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))
    elements.append(table)

    elements.append(Spacer(1, 12))
    
    # Add Total Amount
    total = Paragraph(f"<b>Total Amount: ${total_amount:.2f}</b>", ParagraphStyle(name="Total", fontSize=14, spaceAfter=12))
    elements.append(total)

    # Add Footer with Thank You Note
    elements.append(Spacer(1, 24))
    thank_you_note = Paragraph("Thank you for your purchase!", ParagraphStyle(name="Footer", fontSize=12, spaceBefore=12, alignment=1))
    elements.append(thank_you_note)
    
    pdf.build(elements)

    print(f"Receipt generated: {receipt_filename}")

if __name__ == "__main__":
    transaction_id = "123456789"
    date = "2024-08-08"
    customer_name = "Rahul Dey"
    company_name = "ABC productions"
    logo_path = r"C:\Users\Dell\OneDrive\Desktop\MY_PROJECTS\images.png"  # Replace with the actual path to your logo image

    items = [
        {"name": "Shampoo", "quantity": 2, "price": 19.99},
        {"name": "Hair oil", "quantity": 1, "price": 49.99},
        {"name": "Pencil box", "quantity": 3, "price": 5.99},
    ]
    total_amount = sum(item['quantity'] * item['price'] for item in items)

    create_receipt(transaction_id, date, items, total_amount, customer_name, company_name, logo_path)
