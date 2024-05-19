import streamlit as st
from add_data import handle_file_upload
from create_tables import *
from chat_with_sql import initiate_chat
from db_querry import *

# Display custom very large bold text
st.write("<p style='font-size: 48px; font-weight: bold;'>Chat with Sql Data Base</p>", unsafe_allow_html=True)

# Initialize the session state variable 'n' if it does not exist
if 'n' not in st.session_state:
    st.session_state.n = 0

# Define a counter for dynamic key generation
button_counter = 0

# Display different outputs based on the value of 'n'


if st.session_state.n == 0:
    st.write("Choose 1 option")
    button_counter += 1
    if st.button("Upload the file", key=f"upload_button_{button_counter}"):  # Unique key generated dynamically
        st.session_state.n += 2
        

    button_counter += 1
    if st.button("Query Default Files", key=f"query_button_{button_counter}"):  # Unique key generated dynamically
        st.session_state.n += 1
        

elif st.session_state.n == 1:
    st.write("Enter the Question")
    q1 = st.text_input("Enter the Question")
    st.write(q1)
    s = initiate_chat(q1)
    st.write(s)

elif st.session_state.n == 2:
    st.write("Upload the file")
    handle_file_upload()
    button_counter += 1
    if st.button("Proceed", key=f"proceed_button_{button_counter}"):  # Unique key generated dynamically
        st.session_state.n += 1
        

elif st.session_state.n == 3:
    st.write("Creating table")
    built_table()
    button_counter += 1
    if st.button("Upload the data", key=f"upload_data_button_{button_counter}"):  # Unique key generated dynamically
        drop_all_tables()
        setup_database()
        import_csv()
        st.session_state.n += 1
        

elif st.session_state.n == 4:
    st.write("Enter the Question")
    q1 = st.text_input("Enter the Question")
    st.write(q1)
    button_counter += 1
    if st.button("submit", key=f"submit_button_{button_counter}"):  # Unique key generated dynamically
        s = initiate_chat(q1)
        st.write(s)

    button_counter += 1
    if st.button("Another Action", key=f"another_action_button_{button_counter}"):  # Unique key generated dynamically
        st.session_state.n = 0  # Reset the state to initial
