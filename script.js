// Function to show popup
function showPopup(popupId) {
    const popup = document.getElementById(popupId);
    popup.style.display = "block";
}

// Function to handle login form submission
function handleLogin(event) {
    event.preventDefault();
    // Replace this with your actual login logic
    const username = document.getElementById("loginUsername").value;
    const password = document.getElementById("loginPassword").value;
    // Example: check if username and password match some predefined values
    if (username === "example_user" && password === "password123") {
        // Successful login
        hideLoginButtons();
    } else {
        // Failed login
        alert("Invalid username or password");
    }
}

// Function to hide login and sign-up buttons
function hideLoginButtons() {
    const loginButton = document.getElementById("loginButton");
    const signupButton = document.getElementById("signupButton");
    loginButton.style.display = "none";
    signupButton.style.display = "none";
}

// Add event listener for login form submission
document.getElementById("loginForm").addEventListener("submit", handleLogin);
