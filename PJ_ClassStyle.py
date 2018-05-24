from tkinter import *
from tkinter import ttk
import datetime
#import PJ_Functions as func
class Vessel():
	def __init__(self):
		self.root = Tk()
		self.root.title("Project Manager")
		self.root.geometry("1200x800")
		self.mainframe = ttk.Frame(self.root)
		self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
		self.mainframe.columnconfigure(0, weight=1)
		self.mainframe.columnconfigure(1, weight=1, minsize=300)
		self.mainframe.columnconfigure(2, weight=1, minsize=300)
		self.mainframe.columnconfigure(3, weight=1, minsize=200)
		self.mainframe.columnconfigure(4, weight=1, minsize=200)
		self.mainframe.rowconfigure(0, weight=1)
		self.mainframe.rowconfigure(1, weight=1)
		self.mainframe.rowconfigure(2, weight=1)
		self.mainframe.rowconfigure(3, weight=1)
		self.mainframe.rowconfigure(4, weight=1)
		self.mainframe.rowconfigure(5, weight=1)

		#Vessel information frame
		self.vessel_info()

		#Project costs frame
		self.proj_costs()

		#Operations frame
		self.operation()

		#Finances frame
		self.finances()

		#Finance-rates frame
		self.financerates()

		#Annual figures frame
		self.annual_figures()

		#Loans frame
		self.loan1_frame()

		#Grid/Layout setup
		self.gridsetup()

		#Main loop
		self.root.mainloop()  
#---------------------------------------------------------------------------------------------

#Vessel information frame
	def vessel_info(self, *args):
		year = datetime.date.today().year
		self.projectname = StringVar()
		self.startyear = IntVar(value=year)
		self.project_end = IntVar(value=year+1)
		self.duration = IntVar(value=1)

		self.ship_info = ttk.Labelframe(self.mainframe, text="Vessel information")
		self.ship_info.grid(column=1, row=1, sticky=(N, W, E, S))
		self.ship_info.columnconfigure(1, minsize=120)
		self.ship_info.columnconfigure(2, minsize=75)

		ttk.Label(self.ship_info, text="Project name").grid(column=1, row=1, sticky=W)
		ttk.Entry(self.ship_info, textvariable=self.projectname).grid(column=2, row=1, sticky=(W, E))

		ttk.Label(self.ship_info, text="Project start").grid(column=1, row=2, sticky=W)
		Spinbox(self.ship_info, from_=year, to=year + 45, textvariable=self.startyear).grid(column=2, row=2, sticky=(W, E))

		ttk.Label(self.ship_info, text="Project end").grid(column=1, row=3, sticky=W)
		Spinbox(self.ship_info, from_=year + 1, to=year + 45, textvariable=self.project_end).grid(column=2, row=3, sticky=(W, E))

		ttk.Label(self.ship_info, text="Duration").grid(column=1, row=4, sticky=W)
		dur = ttk.Label(self.ship_info, textvariable=self.duration)
		dur.grid(column=2, row=4, sticky=(W, E))

		#Trace changes and execute function
		self.startyear.trace("w", self.get_duration)
		self.project_end.trace("w", self.get_duration)
		self.duration.trace("w", self.annual_figures_rows)
	#---------------------------------------------------------------------------------------------

	#Project costs frame
	def proj_costs(self, *args):
		self.vesselprice = IntVar()
		self.othercosts = IntVar()
		self.workingcapital = IntVar()
		self.total = IntVar()
		self.salesprice = IntVar()

		self.project_costs = ttk.Labelframe(self.mainframe, text="Project costs")
		self.project_costs.grid(column=1, row=2, sticky=(N, W, E, S))
		self.project_costs.columnconfigure(1, minsize=120)   # Set minsize of column 1 to 120px
		self.project_costs.columnconfigure(2, minsize=75)   # Set minsize of column 1 to 120px

		ttk.Label(self.project_costs, text="Vessel price").grid(column=1, row=1, sticky=W)
		vessel_price = ttk.Entry(self.project_costs, textvariable=self.vesselprice)
		vessel_price.grid(column=2, row=1, sticky=(W, E))

		ttk.Label(self.project_costs, text="Other costs").grid(column=1, row=2, sticky=W)
		other_costs = ttk.Entry(self.project_costs, textvariable=self.othercosts)
		other_costs.grid(column=2, row=2, sticky=(W, E))

		ttk.Label(self.project_costs, text="Working capital").grid(column=1, row=3, sticky=W)
		working_capital = ttk.Entry(self.project_costs, textvariable=self.workingcapital)
		working_capital.grid(column=2, row=3, sticky=(W, E))

		ttk.Label(self.project_costs, text="Total costs").grid(column=1, row=4, sticky=W)
		total_ = ttk.Label(self.project_costs, textvariable=self.total)
		total_.grid(column=2, row=4, sticky=(W, E))

		ttk.Label(self.project_costs, text="Salesprice").grid(column=1, row=5, sticky=W)
		sales_price = ttk.Entry(self.project_costs, textvariable=self.salesprice)
		sales_price.grid(column=2, row=5, sticky=(W, E))

		#Trace changes and execute function
		self.vesselprice.trace("w", self.get_total)
		self.othercosts.trace("w", self.get_total)
		self.workingcapital.trace("w", self.get_total)
	#---------------------------------------------------------------------------------------------

	#Operations frame
	def operation(self, *args):
		self.commission = IntVar()
		self.opcost = IntVar()
		self.escopcost = IntVar()
		self.admincosts = IntVar()
		self.onhiredays = IntVar()

		self.operations = ttk.Labelframe(self.mainframe, text="Operation")
		self.operations.grid(column=2, row=2, sticky=(N, W, E, S))
		self.operations.columnconfigure(1, minsize=120)
		self.operations.columnconfigure(2, weight=1)

		ttk.Label(self.operations, text="Commission rate").grid(column=1, row=1, sticky=W)
		ttk.Label(self.operations, text="0-100%").grid(column=3, row=1, sticky=W)
		comm_rate = ttk.Entry(self.operations, textvariable=self.commission, width=8)
		comm_rate.grid(column=2, row=1, sticky=(W))

		ttk.Label(self.operations, text="Op cost / day").grid(column=1, row=2, sticky=W)
		op_cost = ttk.Entry(self.operations, textvariable=self.opcost, width=8)
		op_cost.grid(column=2, row=2, sticky=(W))

		ttk.Label(self.operations, text="Escalation op cost").grid(column=1, row=3, sticky=W)
		esc_opcost = ttk.Entry(self.operations, textvariable=self.escopcost, width=8)
		esc_opcost.grid(column=2, row=3, sticky=(W))

		ttk.Label(self.operations, text="Adm cost / year").grid(column=1, row=4, sticky=W)
		adm_costs = ttk.Entry(self.operations, textvariable=self.admincosts, width=8)
		adm_costs.grid(column=2, row=4, sticky=(W))

		ttk.Label(self.operations, text="On-hire days").grid(column=1, row=5, sticky=W)
		onhire_days = ttk.Entry(self.operations, textvariable=self.onhiredays, width=8)
		onhire_days.grid(column=2, row=5, sticky=(W))

	#---------------------------------------------------------------------------------------------

	#Financing frame
	def finances(self, *args):
		self.gearing = IntVar()
		self.equity = IntVar()
		self.loans = IntVar()
		self.firstpri = IntVar()

		self.financing = ttk.Labelframe(self.mainframe, text="Financing")
		self.financing.grid(column=1, row=3, sticky=(N, W, E, S))
		self.financing.columnconfigure(1, minsize=120)
		self.financing.columnconfigure(2, minsize=40)

		ttk.Label(self.financing, text="Gearing").grid(column=1, row=1, sticky=W)
		ttk.Label(self.financing, text="0-100%").grid(column=3, row=1, sticky=W)
		ttk.Separator(self.financing, orient=HORIZONTAL).grid(column=1, columnspan=4, row=2, sticky=(W, E))
		gearing_ = ttk.Entry(self.financing, textvariable=self.gearing, width=5)
		gearing_.grid(column=2, row=1, sticky=(W, E))

		ttk.Label(self.financing, text="Equity").grid(column=1, row=3, sticky=W)
		#equity_ = ttk.Entry(self.financing, width=12, textvariable=equity)
		#equity_.grid(column=2, row=2, sticky=(W, E))
		ttk.Label(self.financing, textvariable=self.equity).grid(column=2, row=3, sticky=W, columnspan=2)

		ttk.Label(self.financing, text="Loans").grid(column=1, row=4, sticky=W)
		#loans_ = ttk.Entry(self.financing, width=12, textvariable=loans)
		#loans_.grid(column=2, row=3, sticky=(W, E))
		ttk.Label(self.financing, textvariable=self.loans).grid(column=2, row=4, sticky=W, columnspan=2)

	#---------------------------------------------------------------------------------------------

	#Finance rates frame
	def financerates(self):
		self.firstpri = IntVar()
		self.secpri = IntVar()
		self.interest_depo = IntVar()
		self.interest_overdraft = IntVar()
		self.discount_rate = IntVar()

		self.financerates = ttk.Labelframe(self.mainframe, text="Finance rates")
		self.financerates.grid(column=2, row=3, sticky=(N, W, E, S))
		self.financerates.columnconfigure(1, minsize=100)
		self.financerates.columnconfigure(2, weight=1)

		ttk.Label(self.financerates, text="1st priority loan").grid(column=1, row=1, sticky=W)
		first_pri = ttk.Entry(self.financerates, textvariable=self.firstpri)
		first_pri.grid(column=2, row=1, sticky=(W, E))

		ttk.Label(self.financerates, text="2nd priority loan").grid(column=1, row=2, sticky=W)
		sec_pri = ttk.Entry(self.financerates, textvariable=self.secpri)
		sec_pri.grid(column=2, row=2, sticky=(W, E))

		ttk.Label(self.financerates, text="Interest on deposits").grid(column=1, row=3, sticky=W)
		_interest_depo = ttk.Entry(self.financerates, textvariable=self.interest_depo)
		_interest_depo.grid(column=2, row=3, sticky=(W, E))

		ttk.Label(self.financerates, text="Interest on overdraft").grid(column=1, row=4, sticky=W)
		_interest_overdraft = ttk.Entry(self.financerates, textvariable=self.interest_overdraft)
		_interest_overdraft.grid(column=2, row=4, sticky=(W, E))

		ttk.Label(self.financerates, text="Discount rate").grid(column=1, row=5, sticky=W)
		_discount_rate = ttk.Entry(self.financerates, textvariable=self.discount_rate)
		_discount_rate.grid(column=2, row=5, sticky=(W, E))
		#Trace changes and execute function
		self.gearing.trace("w", self.gearing_ratio)

	#Annual figures frame
	def annual_figures(self, *args):
		self.year = IntVar()
		self.freightrate = IntVar()
		self.dockingdays = IntVar()
		self.dockingcost = IntVar()
		self.rows = IntVar(value=1)

		self.annualfigures = ttk.Labelframe(self.mainframe, text="Annual figures")
		self.annualfigures.grid(column=3, columnspan=2, rowspan=3, row=1, sticky=(N, W, E, S))
		self.annualfigures.columnconfigure(1, minsize=75)
		self.annualfigures.columnconfigure(2, minsize=75)
		self.annualfigures.columnconfigure(3, minsize=75)
		self.annualfigures.columnconfigure(4, minsize=75)

		ttk.Label(self.annualfigures, text="Year").grid(column=1, row=1, sticky=W)
		ttk.Label(self.annualfigures, text="Freight rate").grid(column=2, row=1, sticky=W)
		ttk.Label(self.annualfigures, text="Days in docking").grid(column=3, row=1, sticky=W)
		ttk.Label(self.annualfigures, text="Docking cost").grid(column=4, row=1, sticky=W)

		ttk.Entry(self.annualfigures).grid(column=1, row=2)
		ttk.Entry(self.annualfigures).grid(column=3, row=2)
		ttk.Entry(self.annualfigures).grid(column=4, row=2)
		ttk.Entry(self.annualfigures).grid(column=2, row=2)

		for child in self.annualfigures.winfo_children():
			child.grid_configure(padx=4, pady=2)    #Configures child.grid padding
			if child.__class__ == ttk.Entry:        #Set child.Entry widgets to execute command on focusin
				try:
					child.bind("<FocusIn>", self.select_all)
				except AttributeError:
					pass
			else:
				pass
		for child in self.mainframe.winfo_children(): 
			child.grid_configure(padx=4, pady=2)

		self.rows.trace("w", self.annual_figures_rows)

	def annual_figures_rows(self, *args):
		duration_ = self.duration.get()
		row = self.rows.get()

		if duration_ > row: #Add another row
			ttk.Entry(self.annualfigures).grid(column=1, row=row+2)
			ttk.Entry(self.annualfigures).grid(column=3, row=row+2)
			ttk.Entry(self.annualfigures).grid(column=4, row=row+2)
			ttk.Entry(self.annualfigures).grid(column=2, row=row+2)
			self.rows.set(row + 1)
		if duration_ < row: #Remove row
			for entry in self.annualfigures.grid_slaves():
				if entry.grid_info()['row'] > row:
					entry.destroy()
			self.rows.set(row - 1)
			
		for child in self.annualfigures.winfo_children():
			child.grid_configure(padx=4, pady=2)    #Configures child.grid padding
			if child.__class__ == ttk.Entry:        #Set child.Entry widgets to execute command on focusin
				try:
					child.bind("<FocusIn>", self.select_all)
				except AttributeError:
					pass
			else:
				pass
		for child in self.mainframe.winfo_children(): 
			child.grid_configure(padx=4, pady=2)

	#---------------------------------------------------------------------------------------------

	#Loans frame
	def loan1_frame(self, *args):
		self.loansize = IntVar()
		self.loan_duration = IntVar()
		self.balloondur = IntVar()
		self.balloon = IntVar()
		self.yearlyinst = IntVar()

		self.loan_one = ttk.Labelframe(self.mainframe, text="1st Priority mortage loan")
		self.loan_one.grid(column=1, row=5, sticky=(N, W, E, S))
		self.loan_one.columnconfigure(1, minsize=120)
		self.loan_one.columnconfigure(2, minsize=75)

		ttk.Label(self.loan_one, text="Loan amount").grid(column=1, row=2, sticky=W)
		loan_size = ttk.Entry(self.loan_one, textvariable=self.loansize)
		loan_size.grid(column=2, row=2, sticky=(W, E))

		ttk.Label(self.loan_one, text="Duration").grid(column=1, row=3, sticky=W)
		duration = ttk.Entry(self.loan_one, textvariable=self.loan_duration)
		duration.grid(column=2, row=3, sticky=(W, E))

		ttk.Label(self.loan_one, text="Ballon after X years").grid(column=1, row=4, sticky=W)
		Spinbox(self.loan_one, textvariable=self.balloondur, from_=0, to=25).grid(column=2, row=4, sticky=(W, E))

		ttk.Label(self.loan_one, text="Balloon").grid(column=1, row=5, sticky=W)
		balloon_ = ttk.Entry(self.loan_one, textvariable=self.balloon)
		balloon_.grid(column=2, row=5, sticky=(W, E))

		ttk.Label(self.loan_one, text="Yearly installments").grid(column=1, row=6, sticky=W)
		yearly_inst = ttk.Entry(self.loan_one, textvariable=self.yearlyinst)
		yearly_inst.grid(column=2, row=6, sticky=(W, E))
	#---------------------------------------------------------------------------------------------

	#Functions
	def gridsetup(self):
		for child in self.mainframe.winfo_children(): 
			child.grid_configure(padx=4, pady=2)

		for child in self.ship_info.winfo_children():
			child.grid_configure(padx=4, pady=2)    #Configures child.grid padding
			if child.__class__ == ttk.Entry:        #Set Child.Entry widgets to execute command on focusin
				try:
					child.bind("<FocusIn>", self.select_all)
				except AttributeError:
					pass
			else:
				pass

		for child in self.project_costs.winfo_children():
			child.grid_configure(padx=4, pady=2)    #Configures child.grid padding
			if child.__class__ == ttk.Entry:        #Set Child.Entry widgets to execute command on focusin
				try:
					child.bind("<FocusIn>", self.select_all)
				except AttributeError:
					pass
			else:
				pass

		for child in self.operations.winfo_children():
			child.grid_configure(padx=4, pady=2)    #Configures child.grid padding
			if child.__class__ == ttk.Entry:        #Set Child.Entry widgets to execute command on focusin
				try:
					child.bind("<FocusIn>", self.select_all)
				except AttributeError:
					pass
			else:
				pass

		for child in self.financing.winfo_children():
			child.grid_configure(padx=4, pady=2)    #Configures child.grid padding
			if child.__class__ == ttk.Entry:        #Set Child.Entry widgets to execute command on focusin
				try:
					child.bind("<FocusIn>", self.select_all)
				except AttributeError:
					pass
			else:
				pass

		for child in self.financerates.winfo_children():
			child.grid_configure(padx=4, pady=2)    #Configures child.grid padding
			if child.__class__ == ttk.Entry:        #Set child.Entry widgets to execute command on focusin
				try:
					child.bind("<FocusIn>", self.select_all)
				except AttributeError:
					pass
			else:
				pass

		''' ##Executed in annual_figures method##
		for child in self.annualfigures.winfo_children():
			child.grid_configure(padx=4, pady=2)    #Configures child.grid padding
			if child.__class__ == ttk.Entry:        #Set child.Entry widgets to execute command on focusin
				try:
					child.bind("<FocusIn>", self.select_all)
				except AttributeError:
					pass
			else:
				pass '''

		for child in self.loan_one.winfo_children():
			child.grid_configure(padx=4, pady=2)    #Configures child.grid padding
			if child.__class__ == ttk.Entry:        #Set child.Entry widgets to execute command on focusin
				try:
					child.bind("<FocusIn>", self.select_all)
				except AttributeError:
					pass
			else:
				pass

	def get_duration(self, *args):
		try:
			end = self.project_end.get() - self.startyear.get()
			self.duration.set(end)
		except ValueError:
			pass

	''' def get_project_end(self, *args):
		try:
			value = self.startyear.get() + self.duration.get()
			self.project_end.set(value)
		except ValueError:
			pass '''

	def get_total(self, *args):
		try:
			value = self.vesselprice.get() + self.othercosts.get() + self.workingcapital.get()
			self.total.set("{:,.2f}".format(value))
			self.gearing_ratio()
		except ValueError:
			pass

	def gearing_ratio(self, *args):
		if int(self.gearing.get()) < 101 and int(self.gearing.get()) >= 0:
			try:
				loan = (int(self.vesselprice.get()) + int(self.othercosts.get()) + self.workingcapital.get()) / 100 * int(self.gearing.get())
				self.loans.set("{:,.2f}".format(loan))
				equi = (int(self.vesselprice.get()) + int(self.othercosts.get()) + self.workingcapital.get()) / 100 * (100 - int(self.gearing.get()))
				self.equity.set("{:,.2f}".format(equi))
			except ValueError:
				pass
		else:
			self.gearing.set(0)
			self.select_all(self)

	def select_all(self, event, *args):
		_focus = self.root.focus_get()
		if _focus.__class__ == ttk.Entry:
			_focus.select_range(0, END)
			#print(_focus + _focus.options)
		else:
			pass

	