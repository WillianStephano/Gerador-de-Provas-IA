# 🚀 Gerador de Provas com IA

Um sistema que utiliza inteligência artificial (Google Gemini) para criar provas e exercícios personalizados conforme parâmetros educacionais.

![Interface](https://via.placeholder.com/800x400?text=Preview+do+Gerador+de+Provas) *()*

## ✨ Funcionalidades

- Geração automática de questões por disciplina e nível escolar;
- Configuração de dificuldade das quetões (Fácil, Médio, Difícil);
- Tipos de questões: Múltipla Escolha, Dissertativas, Verdadeiro/Falso;
- Saída formatada em JSON para integração com outros sistemas;
- Interface web intuitiva;

## 🛠️ Tecnologias

- **Backend**: Python + Flask
- **IA Generativa**: Google Gemini API
- **Frontend**: HTML5, CSS3, JavaScript

## 📦 Pré-requisitos

- Python 3.10+
- Conta no [Google AI Studio](https://aistudio.google.com/) (para API Key)
- Node.js

## 🚀 Como Executar

```bash
# 1. Clone o repositório
git clone https://github.com/seu-usuario/gerador-provas-ia.git
cd gerador-provas-ia

# 2. Crie e ative o ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# 3. Instale as dependências
pip install -r backend/requirements.txt

# 4. Configure sua API Key
cp .env.example .env
# Edite o .env com sua GEMINI_API_KEY

# 5. Execute
python backend/run.py