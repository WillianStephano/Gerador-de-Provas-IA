from flask import Blueprint, request, jsonify, render_template
from .ai_service import generate_exercises  # Note o ponto

bp = Blueprint('routes', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/generate', methods=['POST'])
def generate():
    data = request.json
    exercises = generate_exercises(
        data.get('theme', 'Matemática'),
        data.get('level', 'Ensino Médio'),
        data.get('question_type', 'Múltipla Escolha'),
        data.get('difficulty', 'Médio'),
        data.get('quantity', 5)
    )
    return jsonify(exercises)

@bp.route('/results')
def results():
    return render_template('resultados.html')