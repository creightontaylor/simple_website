// Function to handle sign-up link clicks with smooth navigation and error handling
async function handleSignUpLinkClick(event) {
  event.preventDefault();
  try {
    // Assuming there's a function to navigate or perform the sign-up action
    await navigateToSignUpPage();
    console.log('Navigation to sign-up page successful');
  } catch (error) {
    console.error('Failed to navigate to sign-up page:', error);
    // Implement error handling logic here, e.g., display an error message to the user
  }
}

// Attach click event listeners to sign-up links on document load
window.addEventListener('DOMContentLoaded', (event) => {
  document.querySelectorAll('a.sign-up-link').forEach(link => {
    link.addEventListener('click', handleSignUpLinkClick);
  });
});

// Ensure the script is loaded with 'async' or 'defer' to improve loading times
// This should be done in the HTML file where the script tag is included
