import streamlit as st
import json
from pathlib import Path

# -----------------------------
# Data Handling Class
# -----------------------------
class SchoolAdmission:
    database = "school.json"

    def __init__(self):
        self.data = self.load_data()

    def load_data(self):
        if Path(self.database).exists():
            try:
                with open(self.database, "r") as f:
                    return json.load(f)
            except json.JSONDecodeError:
                return []
        return []

    def save_data(self):
        with open(self.database, "w") as f:
            json.dump(self.data, f, indent=4)

    def add_school(self, name, seats):
        # check duplicate
        for s in self.data:
            if s["school_name"].lower() == name.lower():
                return "School already exists!"

        self.data.append({
            "school_name": name,
            "available_seats": seats
        })
        self.save_data()
        return "School added successfully!"

    def admit_student(self, name, seats):
        for s in self.data:
            if s["school_name"].lower() == name.lower():
                if seats > s["available_seats"]:
                    return "Not enough seats available!"
                s["available_seats"] -= seats
                self.save_data()
                return "Admission successful!"
        return "School not found!"

    def cancel_admission(self, name, seats):
        for s in self.data:
            if s["school_name"].lower() == name.lower():
                s["available_seats"] += seats
                self.save_data()
                return "Admission cancelled successfully!"
        return "School not found!"


# -----------------------------
# Streamlit UI
# -----------------------------
st.set_page_config(page_title="School Admission System", layout="centered")

st.title("🏫 School Admission System (Streamlit App)")

app = SchoolAdmission()

menu = st.sidebar.selectbox(
    "Choose Action",
    ["Add School", "Admit Student", "Cancel Admission", "Show Schools"]
)

# -----------------------------
# Add School
# -----------------------------
if menu == "Add School":
    st.subheader("➕ Add School")

    name = st.text_input("School Name")
    seats = st.number_input("Total Seats", min_value=0, step=1)

    if st.button("Add School"):
        result = app.add_school(name, seats)
        st.success(result)

# -----------------------------
# Admit Student
# -----------------------------
elif menu == "Admit Student":
    st.subheader("🎓 Admit Student")

    name = st.text_input("School Name")
    seats = st.number_input("Seats to Admit", min_value=0, step=1)

    if st.button("Admit"):
        result = app.admit_student(name, seats)
        st.info(result)

# -----------------------------
# Cancel Admission
# -----------------------------
elif menu == "Cancel Admission":
    st.subheader("❌ Cancel Admission")

    name = st.text_input("School Name")
    seats = st.number_input("Seats to Cancel", min_value=0, step=1)

    if st.button("Cancel Admission"):
        result = app.cancel_admission(name, seats)
        st.warning(result)

# -----------------------------
# Show Schools
# -----------------------------
elif menu == "Show Schools":
    st.subheader("📋 School List")

    if not app.data:
        st.info("No schools available")
    else:
        for s in app.data:
            st.write(f"🏫 **{s['school_name']}**")
            st.write(f"🎟 Available Seats: {s['available_seats']}")
            st.divider()