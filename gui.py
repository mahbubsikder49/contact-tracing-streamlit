
import streamlit as st
import pika
import json

st.title("Contact Tracing Query System")

person_id = st.text_input("Enter Person Identifier to Query")

if st.button("Submit Query"):
    try:
        parameters = pika.URLParameters(st.secrets["AMQP_URL"])
        connection = pika.BlockingConnection(parameters)
        channel = connection.channel()
        channel.queue_declare(queue='query')
        channel.queue_declare(queue='query-response')

        # Send query
        channel.basic_publish(exchange='', routing_key='query', body=person_id)

        # Receive response
        method_frame, header_frame, body = channel.basic_get(queue='query-response', auto_ack=True)
        if body:
            data = json.loads(body)
            st.success(f"Contacts for {data['person']}: {data['contacts']}")
        else:
            st.warning("No response received. Please try again.")

        connection.close()
    except Exception as e:
        st.error(f"Error: {e}")
