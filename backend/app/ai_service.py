from google import genai
from google.genai import types
from google.genai.types import HarmCategory, HarmBlockThreshold
import json
from .config import Config
import os


class GeminiService:
    def __init__(self):
        try:
            self.client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
            self.available = True
        except Exception as e:
            print(f"Erro ao configurar Gemini: {e}")
            self.available = False

    def generate_exercises(self, tema, nivel, tipo_questao, dificuldade, quantidade):
        if not self.available:
            return self._fallback_response("Serviço Gemini não disponível")

        prompt = f"""
    Você é um especialista em criação de exercícios educacionais. 
    Gere exatamente {quantidade} questões com as seguintes características:
    
    - Tema: {tema}
    - Nível: {nivel}
    - Tipo: {tipo_questao}
    - Dificuldade: {dificuldade}
    
    FORMATO DE SAÍDA OBRIGATÓRIO (JSON):
    {{
        "exercises": [
            {{
                "pergunta": "texto completo da pergunta",
                "resposta": "resposta completa",
                "dificuldade": "{dificuldade}",
                "tipo": "{tipo_questao}",
                "explicacao": "explicação opcional"
            }}
        ]
    }}
    
    Regras importantes:
    1. Retorne APENAS o JSON válido
    2. Não inclua comentários ou texto fora do JSON
    3. Use escape para caracteres especiais
    """

        try:
            response = self.client.models.generate_content(
                model="gemini-2.0-flash",
                contents=[prompt],
                config=types.GenerateContentConfig(
                    max_output_tokens=2000,
                    temperature=0.5,
                    safety_settings=[
                        {
                            "category": HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
                            "threshold": HarmBlockThreshold.BLOCK_NONE
                        },
                        {
                            "category": HarmCategory.HARM_CATEGORY_HARASSMENT,
                            "threshold": HarmBlockThreshold.BLOCK_NONE
                        },
                        {
                            "category": HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT,
                            "threshold": HarmBlockThreshold.BLOCK_NONE
                        },
                        {
                            "category": HarmCategory.HARM_CATEGORY_HATE_SPEECH,
                            "threshold": HarmBlockThreshold.BLOCK_NONE
                        }
                    ]
                )
            )
            return self._parse_response(response)
        except Exception as e:
            print(f"Erro na geração: {e}")
            return self._fallback_response(str(e))

    def _parse_response(self, response):
        try:
            text = response.text
            if not text:
                raise ValueError("Resposta vazia")

            # Limpeza do texto
            text = text.strip().replace('```json', '').replace('```', '')
            data = json.loads(text)

            if not isinstance(data, dict) or "exercises" not in data:
                raise ValueError("Formato inválido")

            return data

        except json.JSONDecodeError:
            # Tenta extrair JSON de respostas mal formatadas
            start = text.find('{')
            end = text.rfind('}') + 1
            if start >= 0 and end > 0:
                try:
                    return json.loads(text[start:end])
                except:
                    pass
            return self._fallback_response("Resposta em formato inválido")

        except Exception as e:
            return self._fallback_response(str(e))

    def _fallback_response(self, error_msg):
        return {
            "exercises": [{
                "pergunta": f"Erro: {error_msg}",
                "resposta": "Tente novamente mais tarde",
                "dificuldade": "Erro",
                "tipo": "Erro"
            }]
        }


# Uso:
gemini = GeminiService()
gemini_service = GeminiService()
generate_exercises = gemini_service.generate_exercises  # <--- Exportação