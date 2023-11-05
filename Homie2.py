import tkinter as tk

def submit_form():
    registration_no = registration_no_entry.get()
    full_name = full_name_entry.get()
    dob = dob_entry.get()
    gender = gender_entry.get()
    nationality = nationality_entry.get()
    contact_number = contact_number_entry.get()
    email = email_entry.get()
    date_of_registration = date_of_registration_entry.get()
    address = address_entry.get()
    father_name = father_name_entry.get()
    parent_contact = parent_contact_entry.get()
    previous_school = previous_school_entry.get()

    # Here you can save this information to your spreadsheet

root = tk.Tk()
root.title("Registration Form")

# Create labels and entry fields for each piece of information
labels = ['Registration No.', 'Full Name', 'Date of Birth', 'Gender', 'Nationality', 
          'Contact Number', 'Email Address', 'Date of Registration', 'Address', 
          "Father's Name", 'Parent / Guardian Contact No.', 'Previous School/ Institution']

entries = []

for i, label_text in enumerate(labels):
    label = tk.Label(root, text=label_text)
    label.grid(row=i, column=0, sticky='w', padx=10, pady=5)
    entry = tk.Entry(root)
    entry.grid(row=i, column=1, padx=10, pady=5)
    entries.append(entry)

# Button to submit the registration form
submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.grid(row=len(labels), columnspan=2, pady=10)

# Retrieve the information entered in the form
registration_no_entry, full_name_entry, dob_entry, gender_entry, nationality_entry, \
    contact_number_entry, email_entry, date_of_registration_entry, address_entry, \
    father_name_entry, parent_contact_entry, previous_school_entry = entries

root.mainloop()
