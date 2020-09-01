from tkinter import *
from tkinter import ttk

from generate import Generator



# creates window in middle of screen
window = Tk()
window_width = 1200
window_height = 700
window.geometry("+{}+{}".format(int((window.winfo_screenwidth() - window_width) / 2), 
                                int((window.winfo_screenheight() - window_height) / 2)))
window.resizable(False, False)
# configures window
icon = PhotoImage(file="lock.png") 
window.title("Password Generator")
window.iconphoto(False, icon)
window.configure(background="black")
window.geometry(f"{window_width}x{window_height}")

# creates title
title = Label(window, text="Password Generator", bg="black", fg="white", font="none 36 bold")
title.grid(row=0, column=0)



# whitespace
for x in range(1, 5):
    Label(window, text="", bg="black").grid(row=x)

# drop down menu for selecting security of password
sec_frame = LabelFrame(window, bg="black")
sec_frame.grid(row=6, column=0)

security_label = Label(sec_frame, text="Password security:", bg="black", fg="white", font="none 18 bold")
security_label.grid(row=0, column=0)

security_levels = ["Weak", "Medium", "Secure", "Strong"]
comboBox = ttk.Combobox(sec_frame, state="readonly", value=security_levels, width=10, font="none 14")
comboBox.current(2)
comboBox.grid(row=0, column=1)


for x in range(2):
    Label(window, text="", bg="black").grid(row=(7 + x))

# password requirement checkboxes
req_frame = LabelFrame(window, bg="black")
req_frame.grid(row=6, column=1)

req_title = Label(req_frame, text="Password Requirements:", bg="black", fg="white", font="none 24 bold")
req_title.grid(row=0, column=0)

c_check = IntVar()
capital = Checkbutton(req_frame, text="Capital letter", variable=c_check, font="12")
capital.grid(row=1, column=0, sticky="w")

Label(req_frame, bg="black").grid(row=2, column=0)
Label(req_frame, bg="black").grid(row=4, column=0)

s_check = IntVar()
symbol = Checkbutton(req_frame, text="Symbol", variable=s_check, font="12")
symbol.grid(row=3, column=0, sticky="w")

other_frame = LabelFrame(req_frame, bg="black", borderwidth=0)
other_frame.grid(row=5, column=0, sticky="w")

other = Label(other_frame, text="Other:", fg="white", bg="black", font="none 12 bold")
other.grid(row=5, column=0, sticky="w")

def oe_clicked(event):
	other_entry.configure(state=NORMAL, font="none 12 bold", bg="black")
	other_entry.delete(0, END)
	other_entry.unbind("<Button-1>", oe_click_id)

other_entry = Entry(other_frame, bg="black", fg="white", font="12", insertbackground="white", borderwidth=2)
other_entry.insert(0, "Other required characters")
other_entry.configure(state=DISABLED)
other_entry.grid(row=5, column=1, sticky="w")

oe_click_id = other_entry.bind("<Button-1>", oe_clicked)



# password length spinboxes
len_frame = LabelFrame(window, bg="black", padx=10)
len_frame.grid(row=10, column=0)

len_title = Label(len_frame, text=" Password Length ", bg="black", fg="white", font="none 24 bold underline")
len_title.grid(row=0, column=0)

Label(len_frame, text="0 means that there are no password length limitations", fg="white", bg="black").grid(row=1, column=0)


min_frame = LabelFrame(len_frame, borderwidth=0)
min_frame.grid(row=2, column=0, sticky="w")

min_label = Label(min_frame, text="Minimum password length: ", bg="black", fg="white", font="none 12 bold")
min_label.grid(row=2, column=0, sticky="w")

min_spin = Spinbox(min_frame, from_=0, to=50, font="12", bg="black", fg="light gray", width=5)
min_spin.grid(row=2, column=1, sticky="w")

Label(len_frame, bg="black").grid(row=3, column=0)

max_frame = LabelFrame(len_frame, borderwidth=0)
max_frame.grid(row=4, column=0, sticky="w")

max_label = Label(max_frame, text="Maximum password length:", bg="black", fg="white", font="none 12 bold")
max_label.grid(row=1, column=0, sticky="w")

max_spin = Spinbox(max_frame, from_=0, to=100, font="12", bg="black", fg="light gray", width=5)
max_spin.grid(row=1, column=1, sticky="w")


# Generate password button
def generate_pass():
	generate_button.configure(bg="black", fg="white")
	s = security_levels.index(comboBox.get())
	r = "".join(set("" if other_entry.get() == "Other required characters" else other_entry.get()))
	if int(min_spin.get()) > 50:
		min_spin.delete(0, END)
		min_spin.insert(0, 50)
	if int(max_spin.get()) > 100:
		max_spin.delete(0, END)
		max_spin.insert(0, 100)
	a = Generator.generate_password(s, r, int(min_spin.get()), int(max_spin.get()), c_check.get(), s_check.get())

	output.delete(0, END)
	output.insert(0, str(a))
	b = "\n Copy pasted passwords do not save when window is closed"

	if (max_spin.get() != "0") and (int(min_spin.get()) > int(max_spin.get())):
		max_spin.delete(0, END)
		max_spin.insert(0, min_spin.get())
		generate_pass()
			
	else:
		if s == 0:
			note.configure(text="Note: Password made up of adjective, nouns, repeating numbers and required characters" + b)
		elif s == 1:
				if output.get() != "I was too lazy to debug this, just increase the maximum please":
					note.configure(text="Note: First part of password is a slice of the alphabet" + b)
				else:
					note.configure(text=":(")
		elif s == 2:
			if len(output.get()) > 10:
				note.configure(text="Note: This password is hard to remember, best if written down somewhere" + b)
			else:
				note.configure(text="Note: Copy pasted passwords do not save when window is closed")
		else:
			note.configure(text="Note: This password is really hard to remember, best if written down somewhere" + b)

generate_button = Button(window, text="Generate Password", width=16, bg="black", fg="white", borderwidth=5, font="none 30 bold", command=generate_pass)
generate_button.grid(row=10, column=1)


# generated entry box for result
Label(window, bg="black", text="""

					""").grid(row=11, column=0)

g_frame = LabelFrame(window, bg="black")
g_frame.grid(row=12, column=1)

o_label = Label(g_frame, bg="black", text="Generated Password:", fg="white", font="none 18 bold")
o_label.grid(row=0, column=0)

output = Entry(g_frame, bg="black", fg="white", width=70, font="12")
output.grid(row=1, column=0)

note = Label(g_frame, text="Note: ", bg="black", fg="white", font="12")
note.grid(row=2, column=0, sticky="w")


window.mainloop()
