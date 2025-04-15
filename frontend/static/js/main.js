document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("exerciseForm");
  const loading = document.getElementById("loading");
  const resultsDiv = document.getElementById("results");
  let currentExercises = [];

  // Delegation de eventos (resolve o problema definitivamente)
  resultsDiv.addEventListener("click", (event) => {
    if (event.target.id === "downloadPdf") {
      downloadPDF(currentExercises);
    }
    if (event.target.id === "downloadPdfQuestions") {
      downloadPDFQuestions(currentExercises);
    }
  });

  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    loading.style.display = "block";
    resultsDiv.innerHTML = "";

    const formData = {
      theme: document.getElementById("theme").value,
      subject: document.getElementById("subject").value,
      level: document.getElementById("level").value,
      question_type: document.getElementById("question_type").value,
      difficulty: document.getElementById("difficulty").value,
      quantity: document.getElementById("quantity").value,
    };

    try {
      const response = await fetch("/generate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(formData),
      });

      currentExercises = (await response.json()).exercises || [];
      displayResults(currentExercises);
    } catch (error) {
      resultsDiv.innerHTML = `<p class="error">Erro: ${error.message}</p>`;
    } finally {
      loading.style.display = "none";
    }
  });

  function displayResults(exercises) {
    if (!exercises?.length) {
      resultsDiv.innerHTML = "<p>Nenhum exercício gerado.</p>";
      return;
    }

    resultsDiv.innerHTML = `
            <h2>Exercícios Gerados</h2>
            ${exercises
              .map(
                (ex, i) => `
                <div class="exercise-card">
                    <div class="exercise-meta">
                        <span class="exercise-number">#${i + 1}</span>
                        <span class="exercise-difficulty">${
                          ex.dificuldade || "N/A"
                        }</span>
                        <span class="exercise-type">${ex.tipo || "N/A"}</span>
                    </div>
                    <div class="exercise-question">${ex.pergunta}</div>
                    <div class="exercise-answer"><strong>Resposta:</strong> ${
                      ex.resposta
                    }</div>
                </div>
            `
              )
              .join("")}
            <button id="downloadPdf" class="pdf-button">
                📥 Baixar Prova Completa em PDF
            </button>
            <button id="downloadPdfQuestions" class="pdf-button">
                📥 Baixar Apenas Questoes em PDF
            </button>
        `;
  }

  async function downloadPDF(exercises) {
    try {
      const response = await fetch("/generate-pdf", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ exercises }),
      });

      if (!response.ok) throw new Error(await response.text());

      const blob = await response.blob();
      const url = URL.createObjectURL(blob);
      const a = document.createElement("a");
      a.href = url;
      a.download = `prova_${new Date().toISOString().slice(0, 10)}.pdf`;
      a.click();
      setTimeout(() => URL.revokeObjectURL(url), 100);
    } catch (error) {
      console.error("Falha no PDF:", error);
      alert("Erro ao gerar PDF:\n" + error.message);
    }
  }

  async function downloadPDFQuestions(exercises) {
    try {
      const response = await fetch("/generate-pdf-questions", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ exercises }),
      });

      if (!response.ok) throw new Error(await response.text());

      const blob = await response.blob();
      const url = URL.createObjectURL(blob);
      const a = document.createElement("a");
      a.href = url;
      a.download = `prova_${new Date().toISOString().slice(0, 10)}.pdf`;
      a.click();
      setTimeout(() => URL.revokeObjectURL(url), 100);
    } catch (error) {
      console.error("Falha no PDF:", error);
      alert("Erro ao gerar PDF:\n" + error.message);
    }
  }
});
