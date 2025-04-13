from flask import Blueprint, request, jsonify, render_template, Response
from .ai_service import generate_exercises  # Note o ponto
from flask import send_file
from .pdf_generator import generate_pdf

bp = Blueprint('routes', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/generate', methods=['POST'])
def generate():
    data = request.json
    exercises = generate_exercises(
        data.get('theme', 'Matemática'),
        data.get('subject', 'Assunto central'),
        data.get('level', 'Ensino Médio'),
        data.get('question_type', 'Múltipla Escolha'),
        data.get('difficulty', 'Médio'),
        data.get('quantity', 5)
    )
    return jsonify(exercises)

@bp.route('/results')
def results():
    return render_template('resultados.html')


@bp.route('/generate-pdf', methods=['POST'])
def generate_pdf_route():
    try:
        data = request.get_json()
        exercises = data.get('exercises', [])
        
        if not exercises:
            return jsonify({"error": "Nenhum exercício fornecido"}), 400

        pdf_buffer = generate_pdf(exercises)
        
        return Response(
            pdf_buffer,
            mimetype='application/pdf',
            headers={
                "Content-Disposition": "attachment; filename=prova_gerada.pdf",
                "Content-Type": "application/pdf"
            }
        )

    except Exception as e:
        print(f"Erro ao gerar PDF: {str(e)}")
        return jsonify({"error": str(e)}), 500