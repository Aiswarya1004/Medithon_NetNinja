async function createPatient() {
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const mobile = document.getElementById('mobile').value;
    const date = document.getElementById('date').value;
    const note = document.getElementById('note').value;
  

    const response = await fetch('http://127.0.0.1:5000/api/appointments', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            name: name,
            email: email,
            mobile: mobile,
            date: date,
            note: note,

        })
    });
}

document.getElementById('myForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevents the form from submitting and refreshing the page
    // Handle form submission via JavaScript
    console.log('Form submitted');
});