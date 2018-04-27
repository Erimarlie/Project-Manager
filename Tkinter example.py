from tkinter import *
from tkinter import ttk
import datetime

def calculate(*args):
    try:
        value = float(feet.get())
        meters.set((0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass
    
def get_duration(*args):
    try:
        end = project_end.get() - startyear.get()
        duration.set(end)
    except ValueError:
        pass

def get_total(*args):
    try:
        value = vesselprice.get() + othercosts.get()
        total.set(value)
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

# Trace changes and execute function
startyear.trace("w", get_duration) 
project_end.trace("w", get_duration)

ship_info = ttk.Labelframe(mainframe, text="Vessel information")
ship_info.grid(column=1, row=1, sticky=(N, W, E, S))
ship_info.columnconfigure(1, minsize=120)

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
vesselprice = IntVar()
othercosts = IntVar()
workingcapital = IntVar()
total = IntVar()
salesprice = IntVar()

# Trace changes and execute function
vesselprice.trace("w", get_total)
othercosts.trace("w", get_total)
workingcapital.trace("w", get_total)

project_costs = ttk.Labelframe(mainframe, text="Project costs")
project_costs.grid(column=1, row=2, sticky=(N, W, E, S))
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
ttk.Label(project_costs, textvariable=total).grid(column=2, row=4, sticky=W)

ttk.Label(project_costs, text="Salesprice").grid(column=1, row=5, sticky=W)
sales_price = ttk.Entry(project_costs, width=25, textvariable=salesprice)
sales_price.grid(column=2, row=5, sticky=(W, E))

"""
---------------------------------------------------------------------------------
Operations frame
---------------------------------------------------------------------------------
"""
commission = StringVar()
opcost = StringVar()
escopcost = StringVar()
admcosts = StringVar()
onhiredays = StringVar()

operations = ttk.Labelframe(mainframe, text="Operation")
operations.grid(column=2, row=2, sticky=(N, W, E, S))
operations.columnconfigure(1, minsize=120)

ttk.Label(operations, text="Commission rate").grid(column=1, row=1, sticky=W)
comm_rate = ttk.Entry(operations, width=25, textvariable=commission)
comm_rate.grid(column=2, row=1, sticky=(W, E))

ttk.Label(operations, text="Op cost / day").grid(column=1, row=2, sticky=W)
op_cost = ttk.Entry(operations, width=25, textvariable=opcost)
op_cost.grid(column=2, row=2, sticky=(W, E))

ttk.Label(operations, text="Escalation op cost").grid(column=1, row=3, sticky=W)
esc_opcost = ttk.Entry(operations, width=25, textvariable=escopcost)
esc_opcost.grid(column=2, row=3, sticky=(W, E))

ttk.Label(operations, text="Adm costs / year").grid(column=1, row=4, sticky=W)
adm_costs = ttk.Entry(operations, width=25, textvariable=admcosts)
adm_costs.grid(column=2, row=4, sticky=(W, E))

ttk.Label(operations, text="On-hire days").grid(column=1, row=5, sticky=W)
onhire_days = ttk.Entry(operations, width=25, textvariable=onhiredays)
onhire_days.grid(column=2, row=5, sticky=(W, E))


"""
---------------------------------------------------------------------------------
Some grid configuration and shit
---------------------------------------------------------------------------------
"""
for child in mainframe.winfo_children(): 
    child.grid_configure(padx=8, pady=4)

for child in ship_info.winfo_children():
    child.grid_configure(padx=8, pady=4)

for child in project_costs.winfo_children():
    child.grid_configure(padx=8, pady=4)

for child in operations.winfo_children():
    child.grid_configure(padx=8, pady=4)

root.mainloop()