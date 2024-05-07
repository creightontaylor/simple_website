// Script to enhance user interaction during sign-up process

document.addEventListener('DOMContentLoaded', function() {
    // Assuming there's a link with the ID 'sign-up-link'
    var signUpLink = document.getElementById('sign-up-link');
    if (signUpLink) {
        signUpLink.addEventListener('click', function(e) {
            e.preventDefault();
            // Display an alert or modal
            alert('Thank you for your interest! You will now be redirected to the sign-up process.');
            // Redirect logic or further interaction can be implemented here
        });
    }
});