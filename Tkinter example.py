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

ship_info = ttk.Labelframe(mainframe, text="Vessel information") # Create labelframe window for vessel information
ship_info.grid(column=1, row=1, sticky=(N, W, E, S))
ship_info.columnconfigure(1, minsize=120)   # Set minsize of column 1 to 120px

ttk.Label(ship_info, text="Project name").grid(column=1, row=1, sticky=W)
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
othercosts = StringVar()
workingcapital = StringVar()

project_costs = ttk.Labelframe(mainframe, text="Project costs")
project_costs.grid(columnspan=2, column=1, row=2, sticky=(N, W, E, S))
project_costs.columnconfigure(1, minsize=120)   # Set minsize of column 1 to 120px

ttk.Label(project_costs, text="Vessel price").grid(column=1, row=1, sticky=W)
vessel_price = ttk.Entry(project_costs, width=25, textvariable=vesselprice)
vessel_price.grid(column=2, row=1, sticky=(W, E))

ttk.Label(project_costs, text="Other costs").grid(column=1, row=2, sticky=W)
other_costs = ttk.Entry(project_costs, width=25, textvariable=othercosts)
other_costs.grid(column=2, row=2, sticky=(W, E))

ttk.Label(project_costs, text="Working capital").grid(column=1, row=3, sticky=W)
working_capital = ttk.Entry(project_costs, width=25, textvariable=workingcapital)
working_capital.grid(column=2, row=3, sticky=(W, E))

ttk.Label(project_costs, text="Total costs").grid(column=1, row=4, sticky=W)


for child in mainframe.winfo_children(): 
    child.grid_configure(padx=8, pady=4)

for child in ship_info.winfo_children():
    child.grid_configure(padx=8, pady=4)

for child in project_costs.winfo_children():
    child.grid_configure(padx=8, pady=4)

root.bind('<Return>', get_end_project)

root.mainloop()