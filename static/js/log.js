
function togglePassword() {
    const passwordField = document.getElementById("id_password");
    const toggleCheckbox = document.getElementById("show-password");

    if (toggleCheckbox.checked) {
        passwordField.type = "text"; // Show the password
    } else {
        passwordField.type = "password"; // Hide the password
    }
}
