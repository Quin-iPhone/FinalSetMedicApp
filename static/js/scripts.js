document.addEventListener('DOMContentLoaded', () => {
    setupFormValidation();
    setupSmoothScrolling();
});

function setupFormValidation() {
    const forms = document.querySelectorAll('form');

    forms.forEach(form => {
        form.addEventListener('submit', event => {
            const inputs = form.querySelectorAll('input, select, textarea');
            let isValid = true;
     .invalid {
         border-color: red;
     }

     .error-message {
         color: red;
         margin-bottom: 1em;
         font-weight: bold;
     }

            // Remove existing error message if any
            const existingError = form.querySelector('.error-message');
            if (existingError) existingError.remove();

            inputs.forEach(input => {
                if (!input.checkValidity()) {
                    isValid = false;
                    input.classList.add('invalid');
                    input.setAttribute('aria-invalid', 'true');
                } else {
                    input.classList.remove('invalid');
                    input.removeAttribute('aria-invalid');
                }
            });

             if (!isValid) {
         inputs[0].scrollIntoView({ behavior: 'smooth', block: 'center' });
     }
{
                event.preventDefault();
                const errorMessage = document.createElement('div');
                errorMessage.textContent = 'Please fill out all required fields correctly.';
                errorMessage.classList.add('error-message');
                form.prepend(errorMessage);
            }
        });
    });
}

function setupSmoothScrolling() {
    const navLinks = document.querySelectorAll('nav a[href^="#"]');

    navLinks.forEach(link => {
        link.addEventListener('click', event => {
            event.preventDefault();
            const targetId = link.getAttribute('href').substring(1);
            const targetElement = document.getElementById(targetId);

            if (targetElement) {
                targetElement.scrollIntoView({ behavior: 'smooth' });
            }
        });
    });
}
