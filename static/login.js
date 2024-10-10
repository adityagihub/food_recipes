function validateForm() {
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;

    // Simple validation
    if (username === "" || password === "") {
        document.getElementById("error-message").innerText = "Username and password are required.";
        return false;
    }

    // You can add more sophisticated validation here if needed

    // For demonstration, redirecting to a success page after validation
    alert("Login successful!"); // Replace with actual login logic
    return true;
}
