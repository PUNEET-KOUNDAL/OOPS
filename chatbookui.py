import streamlit as st

# Initialize session state variables
if 'username' not in st.session_state:
    st.session_state.username = ''
if 'password' not in st.session_state:
    st.session_state.password = ''
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'page' not in st.session_state:
    st.session_state.page = 'menu'

# Menu navigation logic
def go_to(page_name):
    st.session_state.page = page_name

# Home Menu
def show_menu():
    st.title("Welcome to Chatbook 📘")

    st.write("How would you like to proceed?")
    if st.button("1️⃣ Sign Up"):
        go_to('signup')
    if st.button("2️⃣ Sign In"):
        go_to('signin')
    if st.button("3️⃣ Write a Post"):
        go_to('post')
    if st.button("4️⃣ Message a Friend"):
        go_to('message')

# Sign Up page
def show_signup():
    st.title("🔐 Sign Up")

    email = st.text_input("Enter your email")
    password = st.text_input("Enter your password", type='password')

    if st.button("Sign Up"):
        st.session_state.username = email
        st.session_state.password = password
        st.success("You have signed up successfully!")
        go_to('menu')

# Sign In page
def show_signin():
    st.title("🔓 Sign In")

    if st.session_state.username == '' or st.session_state.password == '':
        st.warning("Please sign up first.")
        if st.button("Go to Sign Up"):
            go_to('signup')
    else:
        username = st.text_input("Enter your email")
        password = st.text_input("Enter your password", type='password')
        if st.button("Sign In"):
            if username == st.session_state.username and password == st.session_state.password:
                st.session_state.logged_in = True
                st.success("You are now logged in!")
                go_to('menu')
            else:
                st.error("Incorrect credentials!")

# Post message page
def show_post():
    st.title("📝 Write a Post")

    if st.session_state.logged_in:
        post = st.text_area("Enter your message")
        if st.button("Post"):
            st.success(f"Your post has been published: {post}")
    else:
        st.warning("Please sign in first to post.")
        if st.button("Go to Sign In"):
            go_to('signin')

# Message friend page
def show_message():
    st.title("✉️ Message a Friend")

    if st.session_state.logged_in:
        friend = st.text_input("Enter your friend's name")
        msg = st.text_area("Enter your message")
        if st.button("Send Message"):
            st.success(f"Your message to {friend} has been sent!")
    else:
        st.warning("Please sign in first to message a friend.")
        if st.button("Go to Sign In"):
            go_to('signin')


# Route to appropriate page
if st.session_state.page == 'menu':
    show_menu()
elif st.session_state.page == 'signup':
    show_signup()
elif st.session_state.page == 'signin':
    show_signin()
elif st.session_state.page == 'post':
    show_post()
elif st.session_state.page == 'message':
    show_message()
