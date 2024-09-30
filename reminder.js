async function createReminder() {
    const patient_id = document.getElementById('name').value;
    const medication = document.getElementById('email').value;
    const dosage = document.getElementById('message').value;
    const time = document.getElementById('schedule').value;

    const response = await fetch('http://127.0.0.1:5000/api/reminders', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            patient_id: patient_id,
            medication: medication,
            dosage: dosage,
            time: time,
        })
    });

    if (!response.ok) {
        const errorData = await response.json();
        console.error('Failed to create reminder:', errorData.error);
    } else {
        console.log('Reminder created successfully');
    }
}