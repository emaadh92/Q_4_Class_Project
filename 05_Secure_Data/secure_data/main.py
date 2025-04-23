import streamlit as st
import hashlib 
from cryptography.fernet import Fernet
import os
import time

st.set_page_config(page_title="Secure Data Storage", 
                   page_icon="🔒",
                   layout="wide",
                   initial_sidebar_state="expanded")


if "stored_data" not in st.session_state:
    st.session_state.stored_data = {}

if "failed_attempts" not in st.session_state:
    st.session_state.failed_attempts = 0
 
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if "selected_menu" not in st.session_state:
    st.session_state.selected_menu = "Home"

if "key" not in st.session_state:
    st.session_state.key = os.getenv("FERNET_KEY", Fernet.generate_key())


chiper = Fernet(st.session_state.key)

def hash_password(password):
    """Hash a password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()

def encrypt_data(text, passkey):
    """Encrypt data using Fernet."""
    return chiper.encrypt(text.encode()).decode()

def decrypt_data(encrypted_text, passkey):
    """Decrypt data using Fernet."""
    hashed_passkey = hash_password(passkey)
    for key, value in st.session_state.stored_data.items():
        if value["encrypted_text"] == encrypted_text and value["passkey"] == hashed_passkey:
            st.session_state.failed_attempts = 0
            cipher = Fernet(value["key"])
            try:
                return cipher.decrypt(encrypted_text.encode()).decode()
            except Exception as e:
                st.error(f"Decryption failed. Error: {e}")
                return None
    st.session_state.failed_attempts += 1
    return None


def main():
    with st.sidebar:
        st.title("Secure Data Storage")

        menu = ["Home", "Store Data", "Retrieve Data", "LogIn"]
        choice = st.radio("Select an option", menu , index=0 if st.session_state.failed_attempts >= 3 else 3) 

    if choice == "Home":

        col1, col2 = st.columns([2, 1])
        with col1:
            st.title("Secure Data Encryption System")
            st.markdown(""" 
                <div style='background-color: rgba(141, 17, 17, 0.2); padding: 20px; border-radius: 10px;'>
                    <h3 style='color: #1e88e5;'>Your Personal Digital Safe</h3>
                    <p>Store sensitive information with encryption and retrieve it using your secret passkey.</p>
                    <p style='color: #ff9800;'>No data is stored on disk — full privacy.</p>
                </div>
            """, unsafe_allow_html=True)
            st.markdown("### Features:")
            st.markdown("""
                - **Encryption**: Your data is encrypted using a secure key.
                - **Decryption**: Retrieve your data using the same key.  
                - **Security**: After 3 Attempts, System Down.
            """)
        with col2:
            if os.path.exists("image/lock.jpeg"):
              st.image("image/lock.jpeg", width=200, caption="Secure Data Storage")
            else:
              st.error("Image not found at image/lock.jpeg. Please check the file path and name.")

    elif choice == "Store Data":
        st.title("Store Data")
        col1, col2 = st.columns([3,1])
        with col1:
            user_data = st.text_area("Enter Data" , height=150,
                                     placeholder="Enter your Data here!!!")
            passkey = st.text_input("Enter Passkey", type="password")
            if st.button("Store Data"):
                if user_data and passkey:
                    with st.spinner("Storing data..."):
                        time.sleep(2)
                        hashed = hash_password(passkey)
                        encrypted = encrypt_data(user_data, passkey)
                        st.session_state.stored_data[encrypted] = {
                            "encrypted_text": encrypted,
                            "passkey": hashed,
                            "key": st.session_state.key
                        }
                        st.success("Data encrypted and stored successfully!")
                        st.balloons()
                        st.code(f"Encrypted Data: {encrypted}", language="plaintext") 
                        st.warning("Copy and save this encrypted text and passkey. You'll need both.")
                else:
                    st.error("Please enter both data and passkey.")
        
    elif choice == "Retrieve Data" and not st.session_state.failed_attempts >= 3:
        st.title("Retrieve Data")
        col1, col2 = st.columns([3,1])
        with col1:
            encrpted_input = st.text_area("Enter Encrypted Data", height=150,
                                       placeholder="Enter your Encrypted Data here!!!")
            passkey = st.text_input("Enter Passkey", type="password" 
                                , placeholder="Enter your Passkey here!!!"
                                ,help="Enter the passkey used to encrypt the data.")
            if st.button("Decrypt", key="decrypt_button"):
                if encrpted_input and passkey:
                    with st.spinner("Decrypting data..."):
                        time.sleep(2)
                        decrypted = decrypt_data(encrpted_input, passkey)
                        if decrypted:
                           st.success("Data decrypted successfully!")
                           st.balloons()
                           st.text_area("Decrypted Data", value=decrypted, height=150)
                        else:
                          st.error("Decryption failed. Please check the encrypted data and passkey.")
                        if st.session_state.failed_attempts >= 3:
                           st.warning("Too many failed attempts. Access is restricted.")
                           st.session_state.authenticated = False
                           time.sleep(2)
                           st.experimental_rerun()
                else:
                    st.error("Please enter both encrypted data and passkey.")

    elif choice == "LogIn" or st.session_state.failed_attempts >= 3:
        st.title("Authentication Required")
        col1, col2 = st.columns([1,2])
        with col1:
            if os.path.exists("image/lock.jpeg"):
                st.image("image/lock.jpeg", width=200, caption="Secure Data Storage")
            else:
                st.error("Image not found at image/lock.jpeg. Please check the file path and name.")
        with col2:
            st.warning("You have exceeded the maximum number of attempts.")
            admin_pass =  st.text_input("Enter Admin Passkey", type="password")
            if st.button("Authenticate", key="auth_btn"):
                if admin_pass == os.getenv("ADMIN_PASSWORD", "admin123"):
                    st.session_state.failed_attempts = 0
                    st.session_state.authenticated = True
                    st.success("Authenticated successfully!")
                    st.balloons()
                    time.sleep(2)
                    # st.experimental_rerun()
                else:
                    st.error("Authentication failed. Please try again.") 



# Improved footer with better styling and fixed positioning
st.markdown("""
    <style>
        .footer {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            background-color: #f1f1f1;
            text-align: center;
            padding: 10px 0;
            font-size: 14px;
            color: #333;
            border-top: 1px solid #ddd;
            z-index: 1000;
        }
        .footer a {
            color: #1e88e5;
            text-decoration: none;
        }
        .footer a:hover {
            text-decoration: underline;
        }
    </style>
    <div class="footer">
        © 2025 | Built with ❤️ using <a href='https://streamlit.io/' target='_blank'>Streamlit</a><br>
        Contact: <a href='https://www.linkedin.com/in/muhammad-emad-hassan/'>Muhammad Emad Hassan</a>
    </div>
""", unsafe_allow_html=True)


if __name__ == "__main__":
    main()