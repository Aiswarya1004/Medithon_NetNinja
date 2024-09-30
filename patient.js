async function createPatient() {
    const name = document.getElementById('full_name').value;
    const age = document.getElementById('age').value;
    const gender = document.getElementById('gender').value;
    const contact = document.getElementById('phone').value;
    const emcontact = document.getElementById('emercontact').value;
    const heart_rate = document.getElementById('heart_rate').value;
    const blood_pressure = document.getElementById('blood_pressure').value;
    const temperature = document.getElementById('temperature').value;
    const respiratory_rate = document.getElementById('respiratory_rate').value;
    const oxygen_saturation = document.getElementById('oxygen_saturation').value;
    const past_illnesses = document.getElementById('past_illnesses').value;
    const allergies = document.getElementById('allergies').value;
    const current_medications= document.getElementById('current_medications').value;
    const surgies = document.getElementById('surgeries').value;
    const family_history = document.getElementById('family_history').value;
    const symptoms = document.getElementById('symptoms').value;
    const diagnosis = document.getElementById('diagnosis').value;
    const lab_results = document.getElementById('lab_results').value;

    const response = await fetch('http://127.0.0.1:5000/api/patients', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            name: name,
            age: age,
            gender: gender,
            contact: contact,
            emer_contact: emcontact,
            heart_rate: heart_rate,
            blood_pressure: blood_pressure,
            temperature: temperature,
            resrate: respiratory_rate,
            oxygensat: oxygen_saturation,
            pillness: past_illnesses,
            allergies: allergies,
            current_medications: current_medications,
            previous_surgeries: surgies,
            family_medical: family_history,
            symptoms: symptoms,
            Intial_d: diagnosis,
            lab_t: lab_results
        })
    });
    
    if (!response.ok) {
        console.error('Failed to create patient:', response.statusText);
    }
    console.log(emcontact);
}