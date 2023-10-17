import requests

# Set the URL of the Flask API
api_url = 'https://d395-34-73-129-182.ngrok-free.app/predict'  # Replace with the actual URL

# Define the input data as a JSON object

def model_predict(text_data):
    try:
        data = {'text': text_data}
        response = requests.post(api_url, json=data)
        
        if response.status_code == 200:
            result = response.json()
            output = result['result']
        else: 
            print(f'Error: {response.status_code}')
            output=text_data
    except Exception as e:
        print(f'An error occurred: {str(e)}')
        
    return output
