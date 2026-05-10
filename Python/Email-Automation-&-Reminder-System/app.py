import streamlit as st
import pandas as pd
import os
import plotly.express as px
import warnings
from datetime import datetime

# Filter out the specific Streamlit deprecation warning for use_container_width
warnings.filterwarnings("ignore", message=".*use_container_width.*")
from src.config import Config
from src.utils import load_csv, logger
from src.scheduler import ReminderScheduler

# Page configuration
st.set_page_config(
    page_title="Email Automation Dashboard",
    page_icon="📧",
    layout="wide"
)

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Dashboard", "Contacts", "Reminders", "Run Campaigns", "Reports"])

def show_dashboard():
    st.title("🚀 Automation Dashboard")
    
    # Metrics
    contacts = load_csv(Config.CONTACTS_CSV)
    reminders = load_csv(Config.REMINDERS_CSV)
    reports = load_csv(Config.REPORT_FILE) if os.path.exists(Config.REPORT_FILE) else []
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Contacts", len(contacts))
    col2.metric("Scheduled Reminders", len(reminders))
    col3.metric("Emails Sent", len(reports))
    
    # Recent Activity Chart
    if reports:
        df_reports = pd.DataFrame(reports)
        df_reports['timestamp'] = pd.to_datetime(df_reports['timestamp'])
        fig = px.histogram(df_reports, x="timestamp", color="status", title="Email Delivery Status Over Time")
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No delivery data available yet. Run a campaign to see statistics.")

def show_contacts():
    st.title("👥 Contact Management")
    contacts = load_csv(Config.CONTACTS_CSV)
    df = pd.DataFrame(contacts)
    
    st.subheader("Current Contact List")
    st.dataframe(df, use_container_width=True)
    
    with st.expander("Add New Contact"):
        with st.form("add_contact_form"):
            name = st.text_input("Full Name")
            email = st.text_input("Email Address")
            dept = st.selectbox("Department", ["Sales", "HR", "Operations", "Legal", "Marketing", "Finance"])
            submit = st.form_submit_button("Add Contact")
            
            if submit:
                new_id = int(df['id'].max()) + 1 if not df.empty else 1
                new_row = pd.DataFrame([{"id": str(new_id), "name": name, "email": email, "department": dept}])
                df = pd.concat([df, new_row], ignore_index=True)
                df.to_csv(Config.CONTACTS_CSV, index=False)
                st.success(f"Added {name} successfully!")
                st.rerun()

def show_reminders():
    st.title("⏰ Reminder Schedules")
    reminders = load_csv(Config.REMINDERS_CSV)
    df = pd.DataFrame(reminders)
    
    st.subheader("Scheduled Events")
    st.dataframe(df, use_container_width=True)
    
    with st.expander("Schedule New Reminder"):
        with st.form("add_reminder_form"):
            contact_id = st.text_input("Contact ID")
            r_type = st.selectbox("Reminder Type", ["Payment Reminder", "Meeting Alert", "Task Notification", "Webinar Reminder"])
            r_time = st.text_input("Time (HH:MM)", value="09:00")
            template = st.selectbox("Template", ["reminder_email.html"])
            submit = st.form_submit_button("Schedule")
            
            if submit:
                new_id = int(df['id'].max()) + 1 if not df.empty else 1
                new_row = pd.DataFrame([{
                    "id": str(new_id), 
                    "contact_id": contact_id, 
                    "reminder_type": r_type, 
                    "reminder_time": r_time, 
                    "message_template": template
                }])
                df = pd.concat([df, new_row], ignore_index=True)
                df.to_csv(Config.REMINDERS_CSV, index=False)
                st.success("Reminder scheduled successfully!")
                st.rerun()

def show_campaign_runner():
    st.title("⚡ Run Campaigns")
    
    st.warning(f"Mode: {'DRY-RUN (Safe)' if Config.DRY_RUN else 'LIVE (Sending Real Emails)'}")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Instant Simulation")
        st.write("Trigger all scheduled reminders immediately for testing.")
        if st.button("Start Simulation"):
            with st.spinner("Processing..."):
                scheduler = ReminderScheduler()
                scheduler.run_simulation()
            st.success("Simulation complete! Check logs and reports.")

    with col2:
        st.subheader("Background Scheduler")
        st.write("This would typically run as a background service.")
        st.info("In a real app, this button would toggle a server-side process.")

def show_reports():
    st.title("📊 Delivery Reports")
    if os.path.exists(Config.REPORT_FILE):
        df = pd.read_csv(Config.REPORT_FILE)
        st.dataframe(df, use_container_width=True)
        
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Download Report as CSV",
            data=csv,
            file_name=f"delivery_report_{datetime.now().strftime('%Y%m%d')}.csv",
            mime='text/csv',
        )
    else:
        st.info("No reports found. Run a campaign first.")

# Routing
if page == "Dashboard":
    show_dashboard()
elif page == "Contacts":
    show_contacts()
elif page == "Reminders":
    show_reminders()
elif page == "Run Campaigns":
    show_campaign_runner()
elif page == "Reports":
    show_reports()
