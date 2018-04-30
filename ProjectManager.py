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

def get_project_end(*args):
    try:
        value = startyear.get() + duration.get()
        project_end.set(value)
    except ValueError:
        pass
        
def get_total(*args):
    try:
        value = int(vesselprice.get()) + int(othercosts.get()) + int(workingcapital.get())
        total.set(value)
        gearing_ratio()
    except ValueError:
        pass

def gearing_ratio(*args):
    try:
        loan = (int(vesselprice.get()) + int(othercosts.get()) + 
                int(workingcapital.get())) / 100 * gearing.get()
        loans.set("{:,}".format(loan))
        equi = (int(vesselprice.get()) + int(othercosts.get()) + 
                int(workingcapital.get())) / 100 * gearing.get()
        equity.set("{:,}".format(equi))
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
duration.trace("w", get_project_end)

ship_info = ttk.Labelframe(mainframe, text="Vessel information")
ship_info.grid(column=1, row=1, sticky=(N, W, E, S))
ship_info.columnconfigure(1, minsize=100)

ttk.Label(ship_info, text="Project name").grid(column=1, row=1, sticky=W)
project_name = Entry(ship_info, width=12, textvariable=projectname)
project_name.grid(column=2, row=1, sticky=(W, E))

ttk.Label(ship_info, text="Project start").grid(column=1, row=2, sticky=W)
start_year = Spinbox(ship_info, width=12, from_=year, to=year + 45, textvariable=startyear)
start_year.grid(column=2, row=2, sticky=(W, E))

ttk.Label(ship_info, text="Project end").grid(column=1, row=3, sticky=W)
end = Spinbox(ship_info, width=12, from_=year, to=year + 45, textvariable=project_end)
end.grid(column=2, row=3, sticky=(W, E))

ttk.Label(ship_info, text="Duration").grid(column=1, row=4, sticky=W)
dur = Entry(ship_info, width=12, textvariable=duration)
dur.grid(column=2, row=4, sticky=(W, E))


''' 
---------------------------------------------------------------------------------
Project costs frame
---------------------------------------------------------------------------------
'''
vesselprice = StringVar()
othercosts = StringVar()
workingcapital = StringVar()
total = StringVar()
salesprice = IntVar()

# Trace changes and execute function
vesselprice.trace("w", get_total)
othercosts.trace("w", get_total)
workingcapital.trace("w", get_total)

project_costs = ttk.Labelframe(mainframe, text="Project costs")
project_costs.grid(column=1, row=2, sticky=(N, W, E, S))
project_costs.columnconfigure(1, minsize=100)   # Set minsize of column 1 to 120px

ttk.Label(project_costs, text="Vessel price").grid(column=1, row=1, sticky=W)
vessel_price = ttk.Entry(project_costs, width=12, textvariable=vesselprice)
vessel_price.grid(column=2, row=1, sticky=(W, E))
ttk.Label(project_costs, textvariable=vesselprice).grid(column=3, row=1, sticky=W)

ttk.Label(project_costs, text="Other costs").grid(column=1, row=2, sticky=W)
other_costs = ttk.Entry(project_costs, width=12, textvariable=othercosts)
other_costs.grid(column=2, row=2, sticky=(W, E))

ttk.Label(project_costs, text="Working capital").grid(column=1, row=3, sticky=W)
working_capital = ttk.Entry(project_costs, width=12, textvariable=workingcapital)
working_capital.grid(column=2, row=3, sticky=(W, E))

ttk.Label(project_costs, text="Total costs").grid(column=1, row=4, sticky=W)
ttk.Label(project_costs, textvariable=total).grid(column=2, row=4, sticky=W)

ttk.Label(project_costs, text="Salesprice").grid(column=1, row=5, sticky=W)
sales_price = ttk.Entry(project_costs, width=12, textvariable=salesprice)
sales_price.grid(column=2, row=5, sticky=(W, E))

"""
---------------------------------------------------------------------------------
Operations frame
---------------------------------------------------------------------------------
"""
commission = StringVar()
opcost = StringVar()
escopcost = StringVar()
admincosts = StringVar()
onhiredays = StringVar()

operations = ttk.Labelframe(mainframe, text="Operation")
operations.grid(column=2, row=2, sticky=(N, W, E, S))
operations.columnconfigure(1, minsize=100)

ttk.Label(operations, text="Commission rate").grid(column=1, row=1, sticky=W)
comm_rate = ttk.Entry(operations, width=12, textvariable=commission)
comm_rate.grid(column=2, row=1, sticky=(W, E))

ttk.Label(operations, text="Op cost / day").grid(column=1, row=2, sticky=W)
op_cost = ttk.Entry(operations, width=12, textvariable=opcost)
op_cost.grid(column=2, row=2, sticky=(W, E))

ttk.Label(operations, text="Escalation op cost").grid(column=1, row=3, sticky=W)
esc_opcost = ttk.Entry(operations, width=12, textvariable=escopcost)
esc_opcost.grid(column=2, row=3, sticky=(W, E))

ttk.Label(operations, text="Adm cost / year").grid(column=1, row=4, sticky=W)
adm_costs = ttk.Entry(operations, width=12, textvariable=admincosts)
adm_costs.grid(column=2, row=4, sticky=(W, E))

ttk.Label(operations, text="On-hire days").grid(column=1, row=5, sticky=W)
onhire_days = ttk.Entry(operations, width=12, textvariable=onhiredays)
onhire_days.grid(column=2, row=5, sticky=(W, E))

"""
---------------------------------------------------------------------------------
Finances frame
---------------------------------------------------------------------------------
"""
gearing = IntVar()
equity = DoubleVar()
loans = DoubleVar()

# Trace changes and execute function
gearing.trace("w", gearing_ratio)

financing = ttk.Labelframe(mainframe, text="Financing")
financing.grid(column=1, columnspan=2, row=3, sticky=(N, W, E, S))
financing.columnconfigure(1, minsize=100)

ttk.Label(financing, text="Gearing").grid(column=1, row=1, sticky=W)
gearing_ = ttk.Entry(financing, width=12, textvariable=gearing)
gearing_.grid(column=2, row=1, sticky=(W, E))

ttk.Label(financing, text="Equity").grid(column=1, row=2, sticky=W)
#equity_ = ttk.Entry(financing, width=12, textvariable=equity)
#equity_.grid(column=2, row=2, sticky=(W, E))
ttk.Label(financing, textvariable=equity).grid(column=2, row=2, sticky=W)

ttk.Label(financing, text="Loans").grid(column=1, row=3, sticky=W)
#loans_ = ttk.Entry(financing, width=12, textvariable=loans)
#loans_.grid(column=2, row=3, sticky=(W, E))
ttk.Label(financing, textvariable=loans).grid(column=2, row=3, sticky=W)

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

for child in financing.winfo_children():
    child.grid_configure(padx=8, pady=4)

root.mainloop()