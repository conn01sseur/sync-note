const text = "Sync Note";
const typingTextElement = document.getElementById("typing-text");
const userInput = document.getElementById("user-input");
const instructionElement = document.getElementById("instruction");
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
    animateDeleting();
}

async function animateDeleting() {
    while (index > 0) {
        typingTextElement.textContent = text.substring(0, index - 1);
        index--;
        await delay(200);
    }
}

async function startTyping() {
    if (!localStorage.getItem('textDisplayed')) {
        await animateTyping();
        localStorage.setItem('textDisplayed', 'true');
    }
}

userInput.addEventListener("keypress", function(event) {
    if (event.key === "Enter") {
        event.preventDefault();
        showInstruction();
    }
});

startTyping();
