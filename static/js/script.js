const text = "Sync Note";
const typingTextElement = document.getElementById("typing-text");
const userInput = document.getElementById("user-input");
const inputContainer = document.getElementById("input-container");
let index = 0;

function delay(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

async function animateTyping() {
    while (index < text.length) {
        typingTextElement.textContent += text.charAt(index);
        index++;
        await delay(200);
    }
    inputContainer.classList.remove('hidden');
    await delay(1000);
}

async function animateDeleting() {
    while (index > 0) {
        typingTextElement.textContent = text.substring(0, index - 1);
        index--;
        await delay(200);
    }
}

async function startTyping() {
    await animateTyping();
    localStorage.setItem('textDisplayed');
}

startTyping();

document.getElementById('submit').addEventListener('click', function() {
    const text = document.getElementById('user-input').value;
    localStorage.setItem('savedText', text); // Сохраняем текст
    alert('Текст сохранён!');
});

window.addEventListener('load', function() {
    const savedText = localStorage.getItem('savedText');
    if (savedText) {
        document.getElementById('user-input').value = savedText;
    }
});