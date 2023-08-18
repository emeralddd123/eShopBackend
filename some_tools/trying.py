# from reportlab.lib.pagesizes import letter
# from reportlab.pdfgen import canvas

# def generate_receipt(order_id, items, total):
#     pdf_file = f"receipt_{order_id}.pdf"

#     # Create a canvas (PDF document)
#     c = canvas.Canvas(pdf_file, pagesize=letter)

#     # Set up the receipt content
#     c.setFont("Helvetica", 12)
#     c.drawString(100, 750, "Receipt")
#     c.drawString(100, 720, f"Order ID: {order_id}")

#     y_start = 690
#     for item in items:
#         c.drawString(100, y_start, f"{item['product']} x {item['quantity']}")
#         y_start -= 20

#     c.drawString(100, y_start, f"Total: ${total}")

#     # Save the receipt as a PDF file
#     c.save()

# # Example usage
# order_id = 123
# items = [{"product": "Product 1", "quantity": 2}, {"product": "Product 2", "quantity": 1}]
# total = 50.99

# generate_receipt(order_id, items, total)
