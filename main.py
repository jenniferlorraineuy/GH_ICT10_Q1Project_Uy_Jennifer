from pyscript import display
from js import document

def submit_form(*args):

    name = document.getElementById("full name").value
    email = document.getElementById("valid email").value
    message = document.getElementById("message").value

    
    response = f"Thank you, {name}! Your message has been received. We'll reply to {email} soon."

   
    display(response, target="response")

    
    document.getElementById("contact-form").reset()