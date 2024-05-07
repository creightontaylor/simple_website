// Script to handle sign-up link clicks and display a message

document.addEventListener('DOMContentLoaded', function() {
    var signUpLink = document.getElementById('sign-up-link');
    if (signUpLink) {
        signUpLink.addEventListener('click', function(e) {
            e.preventDefault();
            alert('Thank you for your interest! You will now be redirected to the sign-up process.');
            // Here you can add the redirection logic or further interaction handling
        });
    }
});