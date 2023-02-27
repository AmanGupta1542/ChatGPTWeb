function logSubmit(event) {
    event.preventDefault();
    const val = document.querySelector("[name = 'que']").value;
    const csrf_token = document.querySelector("[name = 'csrfmiddlewaretoken']").value;
    if(val.trim()){
        createMessageDiv(val.trim(), true);
        createLoader();

        // Build formData object.
        let formData = new FormData();
        formData.append('que', val.trim());
        formData.append('csrfmiddlewaretoken', csrf_token);
        fetch('http://127.0.0.1:8000/query',
        {
            body: formData,
            method: 'POST'
        })
        .then((response) => response.json())
        .then((data) => {
            console.log(data)
            console.log(data.data)
            document.getElementById("typing").remove();
            createMessageDiv(data.data)
        });
    }
}

function createLoader(){
    let node = document.createElement("div");
    node.classList.add("dot-typing");
    node.id = "typing";
    // node.style.marginLeft = "15px";
    node.style.cssText = "margin-left: 15px;";
    let bodyDiv = document.getElementsByClassName('body-inner')[0];
    bodyDiv.appendChild(node);
    bodyDiv.scrollIntoView(false)
}

function createMessageDiv(val, user=false){
    // Create an "div" node:
    let bodyDiv = document.getElementsByClassName('body-inner')[0];
    let node = document.createElement("div");
    user ? node.classList.add("message", "user-message") : node.classList.add("message");
    if(user){
        // Create a text node:
        const textnode = document.createTextNode(val);
    
        // Append the text node to the "div" node:
        node.appendChild(textnode);
    } else {
        let i = 0;
        let speed = 50;
        function typeWriter() {
            if (i < val.length) {
                node.innerHTML += val.charAt(i);
                bodyDiv.scrollIntoView(false)
                i++;
                setTimeout(typeWriter, speed);
            }
        }
        typeWriter()
    }
    bodyDiv.appendChild(node);
    bodyDiv.scrollIntoView(false)
    if(user){
        document.querySelector("[name = 'que']").value = '';
    }
}

const form = document.getElementById('queryForm');
form.addEventListener('submit', logSubmit);