
import streamlit as st
import pika
import json
import matplotlib.pyplot as plt

# Grid display function
def display_grid(people, grid_size=(10, 10)):
    fig, ax = plt.subplots()
    ax.set_xlim(0, grid_size[0])
    ax.set_ylim(0, grid_size[1])
    ax.set_xticks(range(grid_size[0]))
    ax.set_yticks(range(grid_size[1]))
    ax.grid(True)

    for person in people:
        x, y = person["x"], person["y"]
        ax.text(x + 0.3, y + 0.3, person["id"], fontsize=12, color='blue')
        ax.plot(x, y, 'o', color='red')

    st.pyplot(fig)

# Streamlit UI
st.title("Contact Tracing Query System with Grid")

# Sample people positions for visualisation (static sample)
people = [
    {"id": "alice", "x": 2, "y": 3},
    {"id": "bob", "x": 5, "y": 5},
    {"id": "eve", "x": 6, "y": 2},
]

# Display static grid
st.subheader("Grid View (Sample Static Positions)")
display_grid(people)

# Query form
st.subheader("Contact Query")
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
