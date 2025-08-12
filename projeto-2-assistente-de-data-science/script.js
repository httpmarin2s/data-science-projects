const apiKeyInput = document.getElementById('apiKey')
const pilarSelect = document.getElementById('pilarSelect')
const questionInput = document.getElementById('questionInput')
const askButton = document.getElementById('askButton')
const form = document.getElementById("form")
const aiResponse = document.getElementById("aiResponse")

// Função para converter markdown em HTML
const markdownToHtml = (text) => {
    const converter = new showdown.Converter()
    return converter.makeHtml(text)
}

// Função para fazer a pergunta à API do Gemini
const perguntarAI = async (question, pilar, apiKey) => {
    const model = "gemini-2.0-flash"
    const baseURL = `https://generativelanguage.googleapis.com/v1beta/models/${model}:generateContent?key=${apiKey}`

    const pergunta = `
Você é um assistente inteligente especializado em Ciência de Dados, com ênfase no pilar "${pilar}". Sua tarefa é responder perguntas sobre esse tema com clareza, empatia e profundidade, como um professor experiente que ensina com paixão.

---

🎯 **Objetivo da resposta:**
Ajudar o usuário a compreender de forma completa o conteúdo perguntado, abordando aspectos:
- Teóricos (explicação clara do conceito)
- Técnicos (aplicações práticas no mundo real e no mercado de trabalho)
- Acadêmicos (como o conceito aparece em cursos, faculdades ou pesquisas)
- Didáticos (usando a Técnica de Feynman para explicar como se fosse para uma criança)

---

📌 **Instruções para responder:**
1. Utilize uma linguagem amigável e envolvente, mesmo nos trechos técnicos.
2. Se não souber a resposta, diga “Não sei” e **não invente**.
3. Se a pergunta **não estiver relacionada à Ciência de Dados**, diga: “Essa pergunta infelizmente não está relacionada com Ciência de Dados.”
4. Use exemplos simples quando possível.
5. Use dados atualizados com base na data de hoje: **${new Date().toLocaleDateString()}**.

---

📝 **Formato da resposta sugerido**: Todas as respostas precisam ter
uma quebra de linha e uma linha divisória que separe os tópicos. Exemplo 

Explicação Teórica: 
RESPOSTA
- Quebra de linha 
- linha horizontal para dividir o tópico

Pergunta: ${question}

---
🧠 Explicação teórica:
Explicação clara e profunda.

---
🛠️ Aplicação técnica:
Exemplo de uso prático no mercado.

---
🎓 Contexto acadêmico:
Como aparece nos cursos.

---
👶 Técnica de Feynman:
Explicação simples como se fosse para uma criança.

---
✅ Pontos-chave para lembrar:
4 a 6 tópicos essenciais.

---
📖 Sugestão de leitura (artigo):
Um link confiável.

---
📚 Sugestão de leitura (livro):
Livro recomendado com explicação.

---
🎥 Sugestão de vídeo no YouTube:
Vídeo confiável e didático.

---
🧩 5 exercícios práticos:
5 perguntas para fixação.

---
Aqui está a pergunta do usuário: ${question}
    `

    const contents = [{
        role: "user",
        parts: [{ text: pergunta }]
    }]

    const tools = [{ google_search: {} }]

    const response = await fetch(baseURL, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ contents, tools })
    })

    const data = await response.json()

    if (!data.candidates || !data.candidates[0]?.content?.parts[0]?.text) {
        throw new Error("Resposta inválida da API")
    }

    return data.candidates[0].content.parts[0].text
}

// Função para lidar com envio do formulário
const enviarFormulario = async (event) => {
    event.preventDefault()

    const apiKey = apiKeyInput.value.trim()
    const pilar = pilarSelect.value.trim()
    const question = questionInput.value.trim()

    if (apiKey === '' || pilar === '' || question === '') {
        alert('Por favor, preencha todos os campos')
        return
    }

    askButton.disabled = true
    askButton.textContent = 'Perguntando...'
    askButton.classList.add('loading')

    try {
        const text = await perguntarAI(question, pilar, apiKey)
        const html = markdownToHtml(text)
        const responseDiv = aiResponse.querySelector('.responsecontent')

        if (responseDiv) {
            responseDiv.innerHTML = html
            aiResponse.style.display = 'block' // Exibe a resposta
        } else {
            console.error("Elemento .responsecontent não encontrado!")
        }

    } catch (error) {
        console.error('Erro ao buscar resposta da IA:', error)
        alert("Erro ao buscar resposta da IA. Verifique sua API Key ou tente novamente.")
    } finally {
        askButton.disabled = false
        askButton.textContent = "Perguntar"
        askButton.classList.remove('loading')
    }
}

// Ativa o envio do formulário
form.addEventListener('submit', enviarFormulario)
