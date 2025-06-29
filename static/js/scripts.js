javascript document
    
    .addEventListener('DOMContentLoaded', function() 
                      {     
                          // Form validation     
                          const forms = document
                              .querySelectorAll('form');     
                          forms
                              .forEach(form => 
                                  {         
                                      form
                                          .addEventListener('submit', function(event) 
                                                            {             
                                                                const inputs = form
                                                                    .querySelectorAll('input, select, textarea');             
                                                                let valid = true;             
                                                                inputs
                                                                    .forEach(input => 
                                                                        {                 
                                                                            if (!input.checkValidity()) 
                                                                            {                     
                                                                                valid = false;                     
                                                                                input
                                                                                    .classList
                                                                                    .add('invalid');                     
                                                                                input
                                                                                    .setAttribute('aria-invalid', 'true');                 
                                                                            } 
                                                                            else 
                                                                            {                    
                                                                                input
                                                                                    .classList
                                                                                    .remove('invalid');                     
                                                                                input
                                                                                    .removeAttribute('aria-invalid');                 
                                                                            }             
                                                                        });             
                                                                if (!valid) 
                                                                {                 
                                                                    event
                                                                        .preventDefault();                 
                                                                    const 
                                                                        errorMessage = document
                                                                        .createElement('div');                 
                                                                    errorMessage
                                                                        .textContent = 'Please fill out all required fields correctly.';                 
                                                                    errorMessage
                                                                        .classList.add('error-message');                 
                                                                    form
                                                                        .prepend(errorMessage);             
                                                                }         
                                                            });     
                                  });      
                          // Smooth scrolling for navigation links     const navLinks = document.querySelectorAll('nav a[href^="#"]');     navLinks.forEach(link => {         link.addEventListener('click', function(event) {             event.preventDefault();             const targetId = this.getAttribute('href').substring(1);             const targetElement = document.getElementById(targetId);             if (targetElement) {                 window.scrollTo({                     top: targetElement.offsetTop,                     behavior: 'smooth'                 });             }         });     }); }); 

