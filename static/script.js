async function generateTutorial() {
    const components = document.querySelector('#components').value;
    const output = document.querySelector('#output');
    output.textContent = 'Cooking a recipe for you...';

    const response = await fetch('/generate', {
        method: 'POST',
        body: new FormData(document.querySelector('#tutorial-form'))
    });
    
    const data = await response.json(); 
    output.textContent = data.output; 

    const historyList = document.querySelector('.recipe-history ul');
    historyList.innerHTML = ''; 
    data.history.forEach(recipe => {
        const li = document.createElement('li');
        li.innerHTML = `<pre style="white-space: pre-wrap;">${recipe}</pre>`;
        historyList.appendChild(li);
    });
}

function copyToClipboard() {
    const output = document.querySelector('#output');
    const textarea = document.createElement('textarea');
    textarea.value = output.textContent;
    document.body.appendChild(textarea);
    textarea.select();
    document.execCommand('copy');
    document.body.removeChild(textarea);
    alert('Copied to clipboard');
}
