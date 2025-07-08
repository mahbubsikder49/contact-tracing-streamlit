
# Contact Tracing Streamlit App

This app allows you to query contacts for a person identifier using a cloud-hosted RabbitMQ server (CloudAMQP).

## How to Use
1. Enter a person identifier (e.g., "Alice")
2. Click "Submit Query"
3. The app will return a list of people they have come into contact with, if any.

The app connects to a shared CloudAMQP server securely using Streamlit Secrets.
