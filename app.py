
import streamlit as st

st.set_page_config(
    page_title="AI Network Management Chatbot",
    page_icon="🌐"
)

knowledge_base = {
    "ip address": "An IP address is a unique address used to identify a device on a network.",
    "dns": "DNS stands for Domain Name System. It converts domain names into IP addresses.",
    "router": "A router connects different networks and forwards data between them.",
    "tcp": "TCP is a reliable protocol that ensures data is delivered correctly.",
    "udp": "UDP is a fast protocol that sends data without guaranteeing delivery.",
    "osi model": "The OSI model has seven layers: Physical, Data Link, Network, Transport, Session, Presentation and Application.",
    "subnet mask": "A subnet mask separates the network part and host part of an IP address.",
    "dhcp": "DHCP automatically assigns IP addresses to devices on a network.",
    "firewall": "A firewall protects a network by controlling incoming and outgoing traffic.",
    "ping": "Ping checks whether another device is reachable over a network.",
    "tcp vs udp": "TCP is reliable and connection-oriented, while UDP is faster and connectionless.",
    "internet not working": "Check your Wi-Fi connection, restart your router, and check your network settings.",
    "slow internet": "Check your signal strength, restart your router, and reduce unnecessary network usage.",
    "no wifi": "Check whether Wi-Fi is enabled and restart your router if needed.",
    "network troubleshooting": "Check cables, Wi-Fi, IP settings, router status and network connectivity."
}

def chatbot_response(question):
    question = question.lower().strip()

    for keyword, answer in knowledge_base.items():
        if keyword in question:
            return answer

    return "Sorry, I could not understand your question. Please ask about IP address, DNS, router, TCP, UDP or network troubleshooting."

st.title("🌐 AI Network Management Chatbot")
st.write("Ask me questions about computer networks.")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

question = st.chat_input("Ask a networking question...")

if question:
    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    answer = chatbot_response(question)

    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })

    st.rerun()

if st.sidebar.button("Clear Chat"):
    st.session_state.messages = []
    st.rerun()

st.sidebar.info("Educational chatbot using Python, Streamlit and keyword matching.")
