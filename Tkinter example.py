from tkinter import *
from tkinter import ttk
import datetime

def calculate(*args):
    try:
        value = float(feet.get())
        meters.set((0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass
    
def get_end_project(*args):
    try:
        end = project_end.get() - startyear.get()
        duration.set(end)
    except ValueError:
        pass

root = Tk()
root.title("Project Manager")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

year = datetime.date.today().year

''' 
---------------------------------------------------------------------------------
Vessel information frame
---------------------------------------------------------------------------------
'''
projectname = StringVar()
startyear = IntVar()
project_end = IntVar()
duration = IntVar()

ship_info = ttk.Labelframe(mainframe, text="Vessel information")
ship_info.grid(columnspan=5, row=1)

ttk.Label(ship_info, text="Project name").grid(column=1, row=1)
project_name = ttk.Entry(ship_info, width=25, textvariable=projectname)
project_name.grid(column=2, row=1, sticky=(W, E))

ttk.Label(ship_info, text="Project start").grid(column=1, row=2, sticky=W)
start_year = Spinbox(ship_info, from_=year, to=year + 25, textvariable=startyear)
start_year.grid(column=2, row=2, sticky=(W, E))

ttk.Label(ship_info, text="Project end").grid(column=1, row=3, sticky=W)
end = Spinbox(ship_info, from_=year, to=year + 25, textvariable=project_end)
end.grid(column=2, row=3, sticky=(W, E))

ttk.Label(ship_info, text="Duration").grid(column=1, row=4, sticky=W)
ttk.Label(ship_info, textvariable=duration).grid(column=2, row=4, sticky=W)

''' 
---------------------------------------------------------------------------------
Project costs frame
---------------------------------------------------------------------------------
'''
vesselprice = StringVar()

project_costs = ttk.Labelframe(mainframe, text="Project costs")
project_costs.grid(columnspan=3, row=2)

ttk.Label(project_costs, text="Vessel price").grid(column=1, row=1)
vessel_price = ttk.Entry(project_costs, width=25, textvariable=vesselprice)
vessel_price.grid(column=2, row=1, sticky=(W, E))


for child in mainframe.winfo_children(): 
    child.grid_configure(padx=12, pady=12)

for child in ship_info.winfo_children():
    child.grid_configure(padx=8, pady=4)

for child in project_costs.winfo_children():
    child.grid_configure(padx=8, pady=4)

root.bind('<Return>', get_end_project)

root.mainloop()