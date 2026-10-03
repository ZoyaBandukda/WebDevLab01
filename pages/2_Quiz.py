import streamlit as st

st.title("What Kind of Coffee Drink Are You?")
st.write("Answer these questions to find out which coffee shop drink matches your personality!")

st.image("Images/icedlatte.jpg", width=200)
st.image("Images/cold_brew.jpg", width=200)
st.image("Images/matcha.jpg", width=200)

# Scores for each coffee type
iced_latte = 0
cold_brew = 0
matcha = 0
cappuccino = 0

# Question 1
q1 = st.radio( #NEW
    "What does your ideal morning look like?",
    ["Slow and cozy", "Up early and productive", "Running late but making it work", "Sleeping as long as possible"]
)
# Score Question 1
if q1 == "Slow and cozy":
    cappuccino += 1
elif q1 == "Up early and productive":
    cold_brew += 1
elif q1 == "Running late but making it work":
    iced_latte += 1
else:
    matcha += 1
# Question 2
q2 = st.slider( #NEW
    "How much energy do you usually have in the morning?",
    1, 10, 5
)
# Score Question 2
if q2 <= 3:
    cappuccino += 1
elif q2 <= 6:
    matcha += 1
elif q2 <= 8:
    iced_latte += 1
else:
    cold_brew += 1
# Question 3
q3 = st.selectbox( #NEW
    "Pick your ideal study environment:",
    ["A quiet library", "A busy coffee shop", "My room with music", "Anywhere with friends"]
)
# Score Question 3
if q3 == "A quiet library":
    matcha += 1
elif q3 == "A busy coffee shop":
    iced_latte += 1
elif q3 == "My room with music":
    cappuccino += 1
else:
    cold_brew += 1
# Question 4
q4 = st.radio(
    "Your friend texts you asking to hang out last minute. What do you do?",
    ["Immediately say yes", "Check my schedule first", "Suggest something chill", "Probably say no and stay home"]
)
# Score Question 4
if q4 == "Immediately say yes":
    iced_latte += 1
elif q4 == "Check my schedule first":
    cold_brew += 1
elif q4 == "Suggest something chill":
    matcha += 1
else:
    cappuccino += 1
# Question 5
q5 = st.selectbox(
    "Pick a weekend activity:",
    ["Trying a new restaurant", "Getting ahead on work", "Going out with friends", "Staying in and watching a movie"]
)
# Score Question 5
if q5 == "Trying a new restaurant":
    iced_latte += 1
elif q5 == "Getting ahead on work":
    cold_brew += 1
elif q5 == "Going out with friends":
    matcha += 1
else:
    cappuccino += 1
# Scores for each coffee type
iced_latte = 0
cold_brew = 0
matcha = 0
cappuccino = 0
# Show result
if st.button("Find My Coffee!"): #NEW

    if iced_latte >= cold_brew and iced_latte >= matcha and iced_latte >= cappuccino:
        result = "Iced Latte"

    elif cold_brew >= iced_latte and cold_brew >= matcha and cold_brew >= cappuccino:
        result = "Cold Brew"

    elif matcha >= iced_latte and matcha >= cold_brew and matcha >= cappuccino:
        result = "Matcha Latte"

    else:
        result = "Cappuccino"

    st.subheader("Your coffee is...")
    st.write(result)

    if result == "Iced Latte":
        st.write("You're fun, social, and always down to try something new.")

    elif result == "Cold Brew":
        st.write("You're productive, focused, and always have something to get done.")

    elif result == "Matcha Latte":
        st.write("You're calm, balanced, and like doing things at your own pace.")

    else:
        st.write("You're cozy, laid-back, and appreciate the simple things.")
