// Script to enhance user interaction during sign-up process

document.addEventListener('DOMContentLoaded', function() {
    // Assuming there's a link with the ID 'sign-up-link'
    var signUpLink = document.getElementById('sign-up-link');
    if (signUpLink) {
        signUpLink.addEventListener('click', function(e) {
            e.preventDefault();
            // Display a modal or alert before redirecting
            alert('Thank you for your interest! You will now be redirected to the sign-up process.');
            // Redirect to the sign-up page or process
            // window.location.href = 'URL_TO_SIGN_UP_PAGE';
        });
    }
});