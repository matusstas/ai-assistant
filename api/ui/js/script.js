
document.addEventListener('DOMContentLoaded', () => {
    const output = document.getElementById('output');
    const promptInput = document.getElementById('prompt');
    let chatHistory = [];

    marked.setOptions({
        highlight: function (code, lang) {
            if (lang && hljs.getLanguage(lang)) {
                return hljs.highlight(code, { language: lang }).value;
            } else {
                return hljs.highlightAuto(code).value;
            }
        },
        gfm: true,
        breaks: true
    });

    const fileSelect = document.getElementById('file-select');

    let currentFile = localStorage.getItem('selectedFile') || fileSelect.value;
    fileSelect.value = currentFile;

    fileSelect.addEventListener('change', () => {
        localStorage.setItem('selectedFile', fileSelect.value);
        location.reload();
    });

    async function sendMessage() {
        const userPrompt = promptInput.value.trim();
        if (!userPrompt) return;

        document.querySelector('.container').style.justifyContent = 'flex-end';

        const userDiv = document.createElement('div');
        userDiv.className = 'message user-msg';
        userDiv.textContent = userPrompt;
        output.appendChild(userDiv);

        promptInput.value = '';

        console.log(currentFile);

        const payload = {
            file: currentFile,
            text: userPrompt,
            history: chatHistory,
        };

        try {
            const response = await fetch("/api/chat/stream", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(payload)
            });

            if (!response.body) return;

            const reader = response.body.getReader();
            const decoder = new TextDecoder();

            const botDiv = document.createElement('div');
            botDiv.className = 'message bot-msg';
            output.appendChild(botDiv);

            let botBuffer = '';

            while (true) {
                const { value, done } = await reader.read();
                if (done) break;

                const delta = decoder.decode(value, { stream: true });
                botBuffer += delta;

                botDiv.innerHTML = marked.parse(botBuffer);
                botDiv.querySelectorAll('pre code').forEach(block => hljs.highlightElement(block));

                output.scrollTop = output.scrollHeight;

                await new Promise(r => setTimeout(r, 15));
            }

            chatHistory.push({ role: "user", content: userPrompt });
            chatHistory.push({ role: "assistant", content: botBuffer });


        } catch (err) {
            const errorDiv = document.createElement('div');
            errorDiv.className = 'message bot-msg';
            errorDiv.textContent = "Error: " + err.message;
            output.appendChild(errorDiv);
        }
    }

    promptInput.addEventListener('keydown', (e) => {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            sendMessage();
        }
    });

    promptInput.addEventListener('input', () => {
        promptInput.style.height = 'auto';
        promptInput.style.height = promptInput.scrollHeight + 'px';
    });

});