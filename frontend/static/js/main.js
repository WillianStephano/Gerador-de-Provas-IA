document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('exerciseForm');
    const loading = document.getElementById('loading');
    const resultsDiv = document.getElementById('results');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        loading.style.display = 'block';
        resultsDiv.innerHTML = '';

        const formData = {
            theme: document.getElementById('theme').value,
            level: document.getElementById('level').value,
            question_type: document.getElementById('question_type').value,
            difficulty: document.getElementById('difficulty').value,
            quantity: document.getElementById('quantity').value
        };

        try {
            const response = await fetch('/generate', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(formData)
            });

            const data = await response.json();
            displayResults(data.exercises);
        } catch (error) {
            resultsDiv.innerHTML = `<p class="error">Erro ao gerar exercícios: ${error.message}</p>`;
        } finally {
            loading.style.display = 'none';
        }
    });

    function displayResults(exercises) {
        if (!exercises || exercises.length === 0) {
            resultsDiv.innerHTML = '<p>Nenhum exercício foi gerado.</p>';
            return;
        }

        let html = '<h2>Exercícios Gerados</h2>';

        exercises.forEach((ex, index) => {
            html += `
                <div class="exercise-card">
                    <div class="exercise-meta">
                        <span class="exercise-number">#${index + 1}</span>
                        <span class="exercise-difficulty">${ex.dificuldade || 'N/A'}</span>
                        <span class="exercise-type">${ex.tipo || 'N/A'}</span>
                    </div>
                    <div class="exercise-question">${ex.pergunta}</div>
                    <div class="exercise-answer"><strong>Resposta:</strong> ${ex.resposta}</div>
                </div>
            `;
        });

        resultsDiv.innerHTML = html;
    }
});