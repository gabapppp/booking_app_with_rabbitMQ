import concurrent.futures
import requests

# Function to send a single POST request
def send_post_request(url, headers, data):
    try:
        response = requests.post(url, headers=headers, json=data)
        return response.status_code, response.text
    except requests.RequestException as e:
        return None, str(e)

# Function to send parallel POST requests
def send_parallel_post_requests(url, headers, data_list, max_workers=5):
    results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_data = {executor.submit(send_post_request, url, headers, data): data for data in data_list}
        for future in concurrent.futures.as_completed(future_to_data):
            data = future_to_data[future]
            try:
                result = future.result()
            except Exception as exc:
                result = (None, str(exc))
            results.append(result)
    return results

# Function to load emails from a file
def load_emails_from_file(file_path):
    emails = []
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        for line in file:
            emails.append(line.strip())
    return emails

# Function to create data payloads from emails
def create_data_payloads(emails):
    data_template = {
        "password": "Admin@12345",
        "name": "John",
        "role": 0,
        "passportNumber": "12345678"
    }
    data_list = []
    for email in emails:
        data = data_template.copy()
        data["email"] = email
        data_list.append(data)
    return data_list

# Example usage
if __name__ == '__main__':
    url = 'http://localhost:3333/api/v1/user/create'  # Replace with your actual URL
    file_path = 'rockyou.txt'  # Path to your email file
    
    # Load emails from file
    emails = load_emails_from_file(file_path)

    # Create data payloads from emails
    data_list = create_data_payloads(emails)

    # Define headers
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOjEsImlhdCI6MTcxNzQyMTg3OSwiZXhwIjoxNzE3NDIzNjc5LCJ0eXBlIjowfQ.pcDFonQa_JwCxTJIwYrcy-kS9BUvu74qVxTya35gTUg'  # Replace with your actual access token
    }
    
    # Send parallel POST requests
    results = send_parallel_post_requests(url, headers, data_list, max_workers=5)
    
    # Print results
    for status_code, response_text in results:
        print(f'Status Code: {status_code}, Response: {response_text}')
