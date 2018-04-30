from tkinter import *
from tkinter import ttk
from PJ_ClassStyle import Vessel


def get_duration(*args):
        try:
            end = self.project_end.get() - self.startyear.get()
            self.duration.set("{} years".format(end))
        except ValueError:
            pass

''' def get_project_end(*args):
    try:
        value = self.startyear.get() + self.duration.get()
        self.project_end.set(value)
    except ValueError:
        pass '''
            
def get_total(*args):
    try:
        value = int(self.vesselprice.get()) + int(self.othercosts.get()) + self.workingcapital.get()
        self.total.set("{:,}".format(value))
        self.gearing_ratio()
    except ValueError:
        pass

def gearing_ratio(*args):
    if int(self.gearing.get()) < 101 and int(self.gearing.get()) >= 0 and len(self.gearing.get()) < 3:
        try:
            loan = (int(self.vesselprice.get()) + int(self.othercosts.get()) + 
                    self.workingcapital.get()) / 100 * int(self.gearing.get())
            self.loans.set("{:,.2f}".format(loan))
            equi = (int(self.vesselprice.get()) + int(self.othercosts.get()) + 
                    self.workingcapital.get()) / 100 * (100 - int(self.gearing.get()))
            self.equity.set("{:,.2f}".format(equi))
        except ValueError:
            pass
    else:
        self.gearing.set("")