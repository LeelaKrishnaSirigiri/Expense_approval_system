import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

# Page config
st.set_page_config(page_title="Expense Approval System", page_icon="💳", layout="wide")

# --- CSS Styling ---
st.markdown(
    """
    <style>
    /* Body background */
    body {background-color: #f5f5f5;}

    /* Header style */
    .header {
        text-align: center;
        font-size: 40px;
        font-weight: bold;
        color: #2c3e50;
    }
    .subheader {
        text-align: center;
        color: gray;
        margin-bottom: 30px;
    }

    /* Expense card */
    .card {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 15px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        margin-bottom: 10px;
    }

    /* Status colors */
    .status-pending {color: orange; font-weight: bold;}
    .status-approved {color: green; font-weight: bold;}
    .status-rejected {color: red; font-weight: bold;}
    </style>
    """,
    unsafe_allow_html=True
)

# Header
st.markdown('<div class="header">💳 Expense Approval System</div>', unsafe_allow_html=True)
st.markdown('<div class="subheader">Manage employee expenses with proper workflow</div>', unsafe_allow_html=True)

# Sidebar menu
menu = ["Submit Expense", "View Expenses", "Update Expense", "Delete Expense", "Approve/Reject (Manager)"]
choice = st.sidebar.selectbox("Menu", menu)
st.sidebar.markdown("---")
st.sidebar.markdown("**Tips:** Only Pending expenses can be updated/deleted. Approved/Rejected are locked.")

# Helper function to display response nicely
def display_response(response):
    try:
        data = response.json()
    except:
        data = response.text  # fallback if not JSON

    if response.status_code in [200, 201]:
        st.success(data)
    else:
        st.error(data)

# --- Submit Expense ---
if choice == "Submit Expense":
    st.subheader("📝 Submit a New Expense")

    col1, col2 = st.columns(2)

    with col1:
        user_id = st.number_input("User ID", min_value=1, step=1)  # ✅ added
        amount = st.number_input("Amount", min_value=0.01, step=0.01)
        category = st.text_input("Category")

    with col2:
        description = st.text_area("Description")

    if st.button("Submit", key="submit"):
        payload = {
            "user_id": user_id,   # ✅ added
            "amount": amount,
            "category": category,
            "description": description
        }

        response = requests.post(f"{API_URL}/expenses", json=payload)
        display_response(response)

# --- View Expenses ---
elif choice == "View Expenses":
    st.subheader("📄 All Expenses")
    response = requests.get(f"{API_URL}/expenses")
    if response.status_code == 200:
        expenses = response.json()
        if expenses:
            for exp in expenses:
                status_class = "status-pending" if exp["status"]=="Pending" else "status-approved" if exp["status"]=="Approved" else "status-rejected"
                st.markdown(f"""
                    <div class="card">
                        <b>ID:</b> {exp['id']} &nbsp;&nbsp;
                        <b>Amount:</b> ₹{exp['amount']} &nbsp;&nbsp;
                        <b>Category:</b> {exp['category']} &nbsp;&nbsp;
                        <b>Status:</b> <span class="{status_class}">{exp['status']}</span><br>
                        <b>Description:</b> {exp['description']}
                    </div>
                """, unsafe_allow_html=True)
        else:
            st.info("No expenses found.")
    else:
        st.error("Failed to fetch expenses.")

# --- Update Expense ---
elif choice == "Update Expense":
    st.subheader("✏️ Update Expense")
    expense_id = st.number_input("Expense ID", min_value=1, step=1)
    amount = st.number_input("Amount", min_value=0.01, step=0.01, key="upd_amount")
    category = st.text_input("Category", key="upd_category")
    description = st.text_area("Description", key="upd_desc")
    if st.button("Update", key="update"):
        payload = {"amount": amount, "category": category, "description": description}
        response = requests.put(f"{API_URL}/expenses/{expense_id}", json=payload)
        display_response(response)

# --- Delete Expense ---
elif choice == "Delete Expense":
    st.subheader("🗑️ Delete Expense")
    expense_id = st.number_input("Expense ID", min_value=1, step=1, key="del_id")
    if st.button("Delete", key="delete"):
        response = requests.delete(f"{API_URL}/expenses/{expense_id}")
        display_response(response)

# --- Approve/Reject Expense ---
elif choice == "Approve/Reject (Manager)":
    st.subheader("✅ Approve or ❌ Reject Expense")
    expense_id = st.number_input("Expense ID", min_value=1, step=1, key="apr_id")
    status = st.selectbox("Status", ["Approved", "Rejected"], key="apr_status")
    if st.button("Submit", key="approve_reject"):
        payload = {"status": status}
        response = requests.patch(f"{API_URL}/expenses/{expense_id}/status", json=payload)
        display_response(response)