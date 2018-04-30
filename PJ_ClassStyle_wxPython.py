import datetime

import wx


class Vessel():
    def __init__(self):
        root = wx.App()
        self.mainframe = wx.Frame(None, title="Project Manager")
        self.mainframe.Show()
        self.mainframe.grid()
        self.mainframe.columnconfigure(0, weight=1)
        self.mainframe.rowconfigure(0, weight=1)
        #Vessel information frame
        self.projectname = StringVar()
        self.startyear = IntVar()
        self.project_end = IntVar()
        self.duration = IntVar()
        
        #-----------------------------------------------

        #Project costs frame
        self.vesselprice = StringVar()
        self.othercosts = StringVar()
        self.workingcapital = StringVar()
        self.total = StringVar()
        self.salesprice = IntVar()
        
        #-----------------------------------------------

        #Operations frame
        self.commission = StringVar()
        self.opcost = StringVar()
        self.escopcost = StringVar()
        self.admincosts = StringVar()
        self.onhiredays = StringVar()

        #Finances frame
        self.gearing = IntVar()
        self.equity = DoubleVar()
        self.loans = DoubleVar()

        year = datetime.date.today().year

        
        #-----------------------------------------------
        
        #Vessel information frame
        self.ship_info = ttk.Labelframe(self.mainframe, text="Vessel information")
        self.ship_info.grid(column=1, row=1, sticky=(N, W, E, S))
        self.ship_info.columnconfigure(1, minsize=100)

        ttk.Label(self.ship_info, text="Project name").grid(column=1, row=1, sticky=W)
        Entry(self.ship_info, width=12, textvariable=self.projectname
        ).grid(column=2, row=1, sticky=(W, E))

        ttk.Label(self.ship_info, text="Project start").grid(column=1, row=2, sticky=W)
        Spinbox(self.ship_info, width=12, from_=year, to=year + 45, textvariable=self.startyear
        ).grid(column=2, row=2, sticky=(W, E))

        ttk.Label(self.ship_info, text="Project end").grid(column=1, row=3, sticky=W)
        Spinbox(self.ship_info, width=12, from_=year, to=year + 45, textvariable=self.project_end
        ).grid(column=2, row=3, sticky=(W, E))

        ttk.Label(self.ship_info, text="Duration").grid(column=1, row=4, sticky=W)
        Entry(self.ship_info, width=12, textvariable=self.duration
        ).grid(column=2, row=4, sticky=(W, E))

        #Trace changes and execute function
        self.startyear.trace("w", self.get_duration)
        self.project_end.trace("w", self.get_duration)
        self.duration.trace("w", self.get_project_end)
        #-----------------------------------------------

        #Project costs frame
        self.project_costs = ttk.Labelframe(self.mainframe, text="Project costs")
        self.project_costs.grid(column=1, row=2, sticky=(N, W, E, S))
        self.project_costs.columnconfigure(1, minsize=100)   # Set minsize of column 1 to 120px

        ttk.Label(self.project_costs, text="Vessel price"
        ).grid(column=1, row=1, sticky=W)
        vessel_price = ttk.Entry(self.project_costs, width=12, textvariable=self.vesselprice)
        vessel_price.grid(column=2, row=1, sticky=(W, E))
        ttk.Label(self.project_costs, textvariable=self.vesselprice
        ).grid(column=3, row=1, sticky=W)

        ttk.Label(self.project_costs, text="Other costs"
        ).grid(column=1, row=2, sticky=W)
        other_costs = ttk.Entry(self.project_costs, width=12, textvariable=self.othercosts)
        other_costs.grid(column=2, row=2, sticky=(W, E))

        ttk.Label(self.project_costs, text="Working capital"
        ).grid(column=1, row=3, sticky=W)
        working_capital = ttk.Entry(self.project_costs, width=12, textvariable=self.workingcapital)
        working_capital.grid(column=2, row=3, sticky=(W, E))

        ttk.Label(self.project_costs, text="Total costs"
        ).grid(column=1, row=4, sticky=W)
        ttk.Label(self.project_costs, textvariable=self.total).grid(column=2, row=4, sticky=W)

        ttk.Label(self.project_costs, text="Salesprice"
        ).grid(column=1, row=5, sticky=W)
        sales_price = ttk.Entry(self.project_costs, width=12, textvariable=self.salesprice)
        sales_price.grid(column=2, row=5, sticky=(W, E))

        #Trace changes and execute function
        self.vesselprice.trace("w", self.get_total)
        self.othercosts.trace("w", self.get_total)
        self.workingcapital.trace("w", self.get_total)
        #-----------------------------------------------

        #Operations frame
        self.operations = ttk.Labelframe(self.mainframe, text="Operation")
        self.operations.grid(column=2, row=2, sticky=(N, W, E, S))
        self.operations.columnconfigure(1, minsize=100)

        ttk.Label(self.operations, text="Commission rate"
        ).grid(column=1, row=1, sticky=W)
        comm_rate = ttk.Entry(self.operations, width=12, textvariable=self.commission)
        comm_rate.grid(column=2, row=1, sticky=(W, E))

        ttk.Label(self.operations, text="Op cost / day"
        ).grid(column=1, row=2, sticky=W)
        op_cost = ttk.Entry(self.operations, width=12, textvariable=self.opcost)
        op_cost.grid(column=2, row=2, sticky=(W, E))

        ttk.Label(self.operations, text="Escalation op cost"
        ).grid(column=1, row=3, sticky=W)
        esc_opcost = ttk.Entry(self.operations, width=12, textvariable=self.escopcost)
        esc_opcost.grid(column=2, row=3, sticky=(W, E))

        ttk.Label(self.operations, text="Adm cost / year"
        ).grid(column=1, row=4, sticky=W)
        adm_costs = ttk.Entry(self.operations, width=12, textvariable=self.admincosts)
        adm_costs.grid(column=2, row=4, sticky=(W, E))

        ttk.Label(self.operations, text="On-hire days").grid(column=1, row=5, sticky=W)
        onhire_days = ttk.Entry(self.operations, width=12, textvariable=self.onhiredays)
        onhire_days.grid(column=2, row=5, sticky=(W, E))

        #-----------------------------------------------

        #Finances frame
        self.financing = ttk.Labelframe(self.mainframe, text="Financing")
        self.financing.grid(column=1, columnspan=2, row=3, sticky=(N, W, E, S))
        self.financing.columnconfigure(1, minsize=100)

        ttk.Label(self.financing, text="Gearing").grid(column=1, row=1, sticky=W)
        gearing_ = ttk.Entry(self.financing, width=12, textvariable=self.gearing)
        gearing_.grid(column=2, row=1, sticky=(W, E))

        ttk.Label(self.financing, text="Equity").grid(column=1, row=2, sticky=W)
        #equity_ = ttk.Entry(self.financing, width=12, textvariable=equity)
        #equity_.grid(column=2, row=2, sticky=(W, E))
        ttk.Label(self.financing, textvariable=self.equity
        ).grid(column=2, row=2, sticky=W)

        ttk.Label(self.financing, text="Loans"
        ).grid(column=1, row=3, sticky=W)
        #loans_ = ttk.Entry(self.financing, width=12, textvariable=loans)
        #loans_.grid(column=2, row=3, sticky=(W, E))
        ttk.Label(self.financing, textvariable=self.loans
        ).grid(column=2, row=3, sticky=W)

        #Trace changes and execute function
        self.gearing.trace("w", self.gearing_ratio)
        #-----------------------------------------------

        for child in self.mainframe.winfo_children(): 
            child.grid_configure(padx=8, pady=4)

        for child in self.ship_info.winfo_children():
            child.grid_configure(padx=8, pady=4)

        for child in self.project_costs.winfo_children():
            child.grid_configure(padx=8, pady=4)

        for child in self.operations.winfo_children():
            child.grid_configure(padx=8, pady=4)

        for child in self.financing.winfo_children():
            child.grid_configure(padx=8, pady=4)
        mainframe.show()
        root.mainloop()

    def get_duration(self, *args):
        try:
            end = self.project_end.get() - self.startyear.get()
            duration.set(end)
        except ValueError:
            pass

    def get_project_end(self, *args):
        try:
            value = self.startyear.get() + self.duration.get()
            project_end.set(value)
        except ValueError:
            pass
            
    def get_total(self, *args):
        try:
            value = int(self.vesselprice.get()) + int(self.othercosts.get()) + int(self.workingcapital.get())
            self.total.set(value)
            self.gearing_ratio()
        except ValueError:
            pass

    def gearing_ratio(self, *args):
        try:
            loan = (int(self.vesselprice.get()) + int(self.othercosts.get()) + 
                    int(self.workingcapital.get())) / 100 * self.gearing.get()
            self.loans.set("{:,}".format(loan))
            equi = (int(self.vesselprice.get()) + int(self.othercosts.get()) + 
                    int(self.workingcapital.get())) / 100 * (100 - self.gearing.get())
            self.equity.set("{:,}".format(equi))
        except ValueError:
            pass
