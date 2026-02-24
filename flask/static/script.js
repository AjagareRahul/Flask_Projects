
function greet(name) {
    return "Hello, " + name + "!";
}

function showMessage() {
    alert(greet("World"));
}

document.addEventListener('DOMContentLoaded', function() {
    console.log("JavaScript loaded successfully!");
});
