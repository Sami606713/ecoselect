import requests
def send_email(name, phone_nbr, email, msg):
    # Replace these with your Mailgun API key and domain
    api_key = 'pubkey-9340f1f3e35a14da25e025b47b0ef728'
    domain = 'sandboxf93de014108944a482be2c09ee67de1b.mailgun.org'

    # Mailgun API endpoint
    url = f'https://api.mailgun.net/v3/{domain}/messages'

    # Mailgun API request headers
    headers = {
        'Authorization': f'Basic {api_key}',
    }

    # Mailgun API request data
    data={"from": "samiullah <mailgun@sandboxf93de014108944a482be2c09ee67de1b.mailgun.org>",
			"to": ["sami606713@gmail.com", "YOU@YOUR_DOMAIN_NAME"],
			"subject": "Hello",
			"text": "Testing some Mailgun awesomeness!"}

    # Make the Mailgun API request
    response = requests.post(url, headers=headers, data=data)

    # Check if the email was sent successfully (you may need to adjust this based on Mailgun's API response structure)
    if response.status_code == 200:
        print('Email sent successfully!')
    else:
        print(f'Failed to send email. Status code: {response.status_code}')


# send_email('John Doe', '1234567890', 'john.doe@example.com', 'Hello, this is a test message.')


def send_simple_message():
	return requests.post(
		"https://api.mailgun.net/v3/sandboxf93de014108944a482be2c09ee67de1b.mailgun.org/messages",
		auth=("api", "5899add20734f420ddfd047e00cbcd82-4c955d28-c4be5685"),
		data={"from": "samiullah <mailgun@sandboxf93de014108944a482be2c09ee67de1b.mailgun.org>",
			"to": ["sami606713@gmail.com", "samiullah@sandboxf93de014108944a482be2c09ee67de1b.mailgun.org"],
			"subject": "Hello",
			"text": "Testing some Mailgun awesomeness!"})

send_simple_message()
