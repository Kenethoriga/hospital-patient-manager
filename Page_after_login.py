from tkinter import *
from PIL import ImageTk, Image
import Login_PAGE
import AddPatients
import Appoinment_FILE

# Function for the main menu after login
def Page_after_login():
    def addpatients(window):
        window.destroy()
        AddPatients.add_patient()

    def addappointment(window):
        window.destroy()
        Appoinment_FILE.book_appointment()

    def sign_out(window):
        window.destroy()
        Login_PAGE.page()

    # Main menu window setup
    window = Tk()
    window.geometry('1166x718')
    window.resizable(0, 0)
    window.state('zoomed')
    window.title('Dashboard - Agakhan Medical Centre')

    # Background image
    try:
        bg_frame = Image.open('images/hospital1.jpeg')
        bg_photo = ImageTk.PhotoImage(bg_frame)
    except FileNotFoundError:
        print("Error: Background image not found.")
        return

    bg_panel = Label(window, image=bg_photo)
    bg_panel.image = bg_photo
    bg_panel.pack(fill='both', expand='yes')

    # Main Dashboard Frame
    dash_frame = Frame(window, bg='#150220', width=950, height=600)
    dash_frame.place(x=200, y=70)

    # Heading
    txt = "Welcome to Agakhan Medical Centre"
    heading = Label(dash_frame, text=txt, font=('yu gothic ui', 25, "bold"), bg="#9AECF5", fg='black', bd=5, relief=FLAT)
    heading.place(x=80, y=30, width=600, height=45)

    # Add Patients Button
    add_patients_button = Button(
        dash_frame, text="Add Patients", font=("yu gothic ui", 16, "bold"), bg="#FFC107", fg="black", 
        relief=RAISED, command=lambda: addpatients(window)
    )
    add_patients_button.place(x=100, y=150, width=200, height=50)

    # Book Appointment Button
    add_appointment_button = Button(
        dash_frame, text="Book Appointment", font=("yu gothic ui", 16, "bold"), bg="#FFC107", fg="black", 
        relief=RAISED, command=lambda: addappointment(window)
    )
    add_appointment_button.place(x=100, y=250, width=200, height=50)

    # Sign Out Button
    sign_out_button = Button(
        dash_frame, text="Sign Out", font=("yu gothic ui", 16, "bold"), bg="#FF5722", fg="black", 
        relief=RAISED, command=lambda: sign_out(window)
    )
    sign_out_button.place(x=100, y=350, width=200, height=50)

    window.mainloop()

# Main Entry Point
def main():
    window = Tk()
    window.geometry('1166x718')
    window.resizable(0, 0)
    window.state('zoomed')
    window.title('Login Page')

    # Background image
    try:
        bg_frame = Image.open('images/hospital1.jpeg')
        bg_photo = ImageTk.PhotoImage(bg_frame)
    except FileNotFoundError:
        print("Error: Background image not found.")
        return

    bg_panel = Label(window, image=bg_photo)
    bg_panel.image = bg_photo
    bg_panel.pack(fill='both', expand='yes')

    # Login Frame
    lgn_frame = Frame(window, bg='#150220', width=950, height=600)
    lgn_frame.place(x=200, y=70)

    # Heading
    txt = "Agakhan Medical Centre"
    heading = Label(lgn_frame, text=txt, font=('yu gothic ui', 25, "bold"), bg="#9AECF5", fg='black', bd=5, relief=FLAT)
    heading.place(x=80, y=30, width=500, height=45)

    # Left Side Image
    try:
        side_image = Image.open('images/hospt.png').resize((400, 400))
        side_photo = ImageTk.PhotoImage(side_image)
        side_label = Label(lgn_frame, image=side_photo, bg="#150220")
        side_label.image = side_photo
        side_label.place(x=50, y=100)
    except FileNotFoundError:
        print("Error: Side image not found.")
        return

    # Placeholder for functionality, if login is successful, call `Page_after_login`
    Button(lgn_frame, text="Login", font=("yu gothic ui", 16, "bold"), bg="#00C853", fg="white", 
           relief=RAISED, command=lambda: [window.destroy(), Page_after_login()]).place(x=350, y=500, width=200, height=50)

    window.mainloop()

# Run the main program
if __name__ == "__main__":
    main()
