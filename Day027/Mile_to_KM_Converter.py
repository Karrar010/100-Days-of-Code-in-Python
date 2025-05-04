import tkinter

#I HAVE USED HERE ONLY PACK() AND PLACE() LAYOUT MANAGER, ONE CAN ALSO USE GRID() INSTEAD OF PACK()

window = tkinter.Tk()
window.title("Miles to Kilometer Converter")
window.minsize(width=300,height=200)
window.config(padx=10,pady=50)

def convert_miles_to_km():
    miles = float(mile_input.get())
    print(type(miles))
    km_result_text.config(text=round(miles*1.609,2)) #we rewrite the km_result_text and convert the given value

# INPUT OF MILES VALUE
mile_input = tkinter.Entry()
mile_input.pack()
# TEXT TO SHOW CONVERTDED KM VALUE
km_result_text = tkinter.Label(text='0',font=('Arial',12))
km_result_text.pack()

#EXTRA TEXT ON WINDOW
mile_txt = tkinter.Label(text='Miles' ,font=('Arial',12))
mile_txt.place(x=210,y=-5)

is_equal_txt = tkinter.Label(text='is Equal to',font=('Arial',12))
is_equal_txt.place(x=35,y=19)

km_txt = tkinter.Label(text="KM",font=('Arial',12))
km_txt.place(x=170,y=19)

#CALCULATE BUTTON TO CONVERT VALUES
calculate_btn = tkinter.Button(text='Calculate', command= convert_miles_to_km)
calculate_btn.pack()

window.mainloop()