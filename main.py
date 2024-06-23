import streamlit as st

st.title("Exercise: State Management")

st.subheader("Temperature conversion")

# Initialize state with temperatures.
# Use the freezing point of water

if "celsius" not in st.session_state:
    st.session_state['celsius'] = 0.00

if "farenheit" not in st.session_state:
    st.session_state['farenheit'] = 32.00

if "kelvin" not in st.session_state:
    st.session_state['kelvin'] = 273.15

# Write a callback to convert the temperature in Celsius
# to Farenheit and Kelvin. Change the values in the state
# appropriately
def celsius_conversion():
    celsius = st.session_state['celsius']

    st.session_state['farenheit'] = (celsius * 9/5) + 32
    st.session_state['kelvin'] = celsius + 273.15

# Same thing, but converting from Farenheit to Celsius
# and Kelvin
def farenheit_conversion():
    farenheit = st.session_state['farenheit']

    st.session_state['celsius'] = (farenheit - 32) * 5 / 9
    st.session_state['kelvin'] = (farenheit - 32) * 5 / 9 + 273.15

# Same thing, but converting from Kelvin to Celsius
# and Farenheint
def kelvin_conversion():
    kelvin = st.session_state['kelvin']

    st.session_state['celsius'] = (kelvin - 273.15)
    st.session_state['farenheit'] = (kelvin - 273.15) * 9 / 5 + 32

# Write a callback that adds whatever number the user
# inputs to the Celsius box. Use args.

def add_to_celsius(num):
    st.session_state['celsius'] += num
    celsius_conversion()

# Write a callback to sets the temperatures depending on
# which button the user clicks. Use kwargs.

def set_temperatures(celsius, farenheit, kelvin):
    st.session_state['celsius'] = celsius
    st.session_state['farenheit'] = farenheit
    st.session_state['kelvin'] = kelvin

col1, col2, col3 = st.columns(3)


# Hook up the first 3 callbacks to the input widgets
col1.number_input("Celsius", step=0.01, key="celsius", on_change=celsius_conversion)
col2.number_input("Farenheit", step=0.01, key="farenheit", on_change=farenheit_conversion)
col3.number_input("Kelvin", step=0.01, key="kelvin", on_change=kelvin_conversion)

# Hook up the 4th callback to the button. Use args.
col1, _, _ = st.columns(3)
num = col1.number_input("Add to Celsius", step=1)
col1.button("Add", type="primary",
            on_click=add_to_celsius,
            args=(num,))

col1, col2, col3 = st.columns(3)

# Hook up the last callback to each button. Use kwargs.
col1.button('🧊 Freezing point of water',
            on_click=set_temperatures,
            kwargs=dict(celsius=0.00, farenheit=32.00, kelvin=273.15))
col2.button('🔥 Boiling point of water',
            on_click=set_temperatures,
            kwargs=dict(celsius=100.00, farenheit=212.00, kelvin=373.15))
col3.button('🥶 Absolute zero',
            on_click=set_temperatures,
            kwargs=dict(celsius=-273.15, farenheit=-459.67, kelvin=0.00))

st.write(st.session_state)











# import streamlit as st

# st.title("NFL Stats Predictor")
# st.write(st.session_state)
# st.subheader("Predicts fantasy football points")

# st.button("Update")

# # Set value using the key-value syntax
# if "key" not in st.session_state:
#     st.session_state["key"] = "value"

# # Read value from session state
# st.write(f"Reading with key-value syntax: {st.session_state['key']}")

# # Update values in state
# st.session_state['key'] = "new values"

# # Delete item in state
# del st.session_state['key']

# # Set initial value of the widget with the session_state
# if "slider" not in st.session_state:
#     st.session_state["slider"] = 5

# st.slider("Select a number", 0,10, key="slider")

###############################################################################

# from datetime import datetime, timedelta

# st.title("Advanced State Management")

# # Store widget value in session_state
# st.subheader("Store widget value in session_state")

# st.slider("Select a number", 0,10, key="slider")

# st.write(st.session_state)

# # Initialize widget value with session_state

# st.subheader("Initialize widget value with session_state")

# if "num_input" not in st.session_state:
#     st.session_state["num_input"] = 5

# st.number_input("Pick a number", 0,10, key="num_input")

# # Callbacks
# st.subheader("Use Callbacks")

# st.markdown("#### Select your time range")

# def add_timedelta():
#     initial = st.session_state["start_date"]

#     if st.session_state["radio_range"] == "7 days":
#         st.session_state["end_date"] = initial + timedelta(days=7)

#     elif st.session_state["radio_range"] == "28 days":
#         st.session_state["end_date"] = initial + timedelta(days=28)

#     else:
#         pass

# def subtract_timedelta():
#     final = st.session_state['end_date']

#     if st.session_state['end_date'] == '7 days':
#         st.session_state['end_date'] = final + timedelta(days=7)

#     elif st.session_state['end_date'] == '28 days':
#         st.session_state['end_date'] = final + timedelta(days=28)

#     else:
#         pass

# st.radio("Select a range", ["7 days", "28 days", "custom"], horizontal=True, key="radio_range", on_change=add_timedelta)

# col1, col2, col3 = st.columns(3)

# col1.date_input("Start date", key="start_date", on_change=add_timedelta)

# col2.date_input("End date", key="end_date", on_change= subtract_timedelta)
