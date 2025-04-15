import os
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def generate_pdf(exercises):
    """Gera PDF em memória sem criar arquivo temporário"""
    buffer = BytesIO()
    
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    styles = getSampleStyleSheet()
    story = []

    # Conteúdo do PDF
    title = Paragraph("<b>PROVA GERADA</b>", styles['Title'])
    story.append(title)
    story.append(Spacer(1, 24))

    for i, ex in enumerate(exercises, 1):
        question = Paragraph(
            f"<b>Questão {i}:</b> {ex.get('pergunta', '')}",
            styles['BodyText']
        )
        answer = Paragraph(
            f"<b>Resposta:</b> {ex.get('resposta', '')}",
            styles['BodyText']
        )
        story.extend([question, answer, Spacer(1, 12)])

    doc.build(story)
    buffer.seek(0)
    return buffer

def generate_pdf_questions(exercises):
    """Gera PDF em memória sem criar arquivo temporário"""
    buffer = BytesIO()
    
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    styles = getSampleStyleSheet()
    story = []

    # Conteúdo do PDF
    title = Paragraph("<b>PROVA GERADA</b>", styles['Title'])
    story.append(title)
    story.append(Spacer(1, 24))

    for i, ex in enumerate(exercises, 1):
        question = Paragraph(
            f"<b>Questão {i}:</b> {ex.get('pergunta', '')}",
            styles['BodyText']
        )
        story.extend([question, Spacer(1, 12)])

    doc.build(story)
    buffer.seek(0)
    return buffer
