document.addEventListener('DOMContentLoaded', function() {
    // Dynamically load content sections
    document.querySelectorAll('.feature-item').forEach(item => {
        item.addEventListener('click', function(e) {
            const contentId = e.target.getAttribute('data-content-id');
            loadContentSection(contentId);
        });
    });

    // Function to load content dynamically
    function loadContentSection(contentId) {
        const contentSection = document.getElementById(contentId);
        if (contentSection) {
            document.querySelectorAll('.content-section').forEach(section => {
                section.style.display = 'none';
            });
            contentSection.style.display = 'block';
        }
    }

    // Modal window for signing up
    document.getElementById('signup-btn').addEventListener('click', function() {
        showModal('signup-modal');
    });

    document.getElementById('worker-signup-btn').addEventListener('click', function() {
        showModal('worker-signup-modal');
    });

    // Function to show modal windows
    function showModal(modalId) {
        const modal = document.getElementById(modalId);
        if (modal) {
            modal.style.display = 'block';
            // Close modal on close button click
            modal.querySelector('.close').addEventListener('click', function() {
                modal.style.display = 'none';
            });
            // Close modal on outside click
            window.addEventListener('click', function(e) {
                if (e.target == modal) {
                    modal.style.display = 'none';
                }
            });
        }
    }
});
