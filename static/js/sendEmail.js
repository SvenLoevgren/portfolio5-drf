function sendMail(contactForm) {
    emailjs.send("service_71oypo6", "template_5e32put", {
        "from_name": contactForm.name.value,
        "from_email": contactForm.emailaddress.value,
        "message": contactForm.projectsummary.value

    })
    .then(
        function(response) {
            console.log("SUCCESS", response);
            alert("Thanks... your question has been sent. We will get back to you soon!");
        },
        function(error) {
            console.log("FAILED", error);
            alert("There was an error sending your question. Please try again later.");
        }
    );
    return false;  // To block from loading a new page
}