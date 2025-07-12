import streamlit as st
import matplotlib.pyplot as plt

# Mock contact data
mock_contacts = {
    "alice": ["bob", "eve"],
    "bob": ["alice"],
    "eve": ["alice"]
}

# Sample static positions for grid
positions = {
    "alice": (2, 3),
    "bob": (5, 5),
    "eve": (6, 2)
}

# Display grid
st.title("Grid View (Sample Static Positions)")
fig, ax = plt.subplots()
for person, (x, y) in positions.items():
    ax.plot(x, y, 'ro')
    ax.text(x, y + 0.3, person, color='blue', fontsize=12, ha='center')
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.grid(True)
st.pyplot(fig)

# Contact Query Section
st.header("Contact Query")
person_id = st.text_input("Enter Person Identifier to Query")

if st.button("Submit Query"):
    if person_id.lower() in mock_contacts:
        contacts = mock_contacts[person_id.lower()]
        st.success(f"Contacts for {person_id}: {contacts}")
    else:
        st.warning("No contact data found.")

