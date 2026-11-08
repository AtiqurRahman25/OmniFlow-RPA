document.getElementById('autoForm').addEventListener('submit', async function(e) {
    e.preventDefault();

    const submitBtn = document.getElementById('submitBtn');
    submitBtn.disabled = true;
    submitBtn.textContent = 'Submitting...';

    const payload = {
        requestId: "REQ-" + Math.floor(Math.random() * 10000),
        clientName: document.getElementById('clientName').value,
        companyName: document.getElementById('companyName').value,
        targetWebsiteUrl: document.getElementById('targetWebsiteUrl').value,
        actionType: "ExtractData",
        notificationEmail: document.getElementById('notificationEmail').value
    };

    // n8n Webhook URL - POST
    const webhookUrl = 'http://localhost:5678/webhook-test/9524b752-abaa-49f1-8c2a-0d02fe95b3e0';

    try {
        const response = await fetch(webhookUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(payload)
        });

        if (response.ok) {
            alert('Success! Your automation request has been submitted.');
            document.getElementById('autoForm').reset();
        } else {
            alert('Error! Please try again later.');
        }

    } catch (error) {
        console.error('Error:', error);
        alert("We're currently in hibernation mode. We'll respond back to you shortly.");
    } finally {
        submitBtn.disabled = false;
        submitBtn.textContent = 'Submit Request →';
    }
});