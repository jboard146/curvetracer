import customtkinter
#from customtkinter import ttk
import matplotlib
matplotlib.use("TKAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.animation as animation
from matplotlib.figure import Figure
from matplotlib import style
style.use('seaborn-v0_8-whitegrid')

f = Figure(figsize=(20,20), dpi=150, layout='tight')
a = f.add_subplot(111)

def animate(i):
    pullData = open("testdata.txt","r").read()
    dataList = pullData.split('\n')
    xList = []
    yList = []
    for eachLine in dataList:
        if len(eachLine) > 1:
            x, y = eachLine.split(',')
            xList.append(int(x))
            yList.append(int(y))

    print(xList)
    print(yList)

    a.clear()
    a.plot(xList, yList)
    a.set(xlabel="V", ylabel="V")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Curve Tracer")
        self.geometry("800x600")
        self.grid_columnconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)

        self.R1Label = customtkinter.CTkLabel(self, text="Rb/Rg")
        self.R1Label.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nw")
        self.R1Box = customtkinter.CTkEntry(self, placeholder_text="Rb/Rg")
        self.R1Box.grid(row=1, column=0, padx=10, pady=0, sticky="nw")
        self.R2Label = customtkinter.CTkLabel(self, text="Rc/Rs")
        self.R2Label.grid(row=2, column=0, padx=10, pady=(10, 0), sticky="nw")
        self.R2Box = customtkinter.CTkEntry(self, placeholder_text="Rc/Rs")
        self.R2Box.grid(row=3, column=0, padx=10, pady=0, sticky="nw")
        
        self.MinLabel = customtkinter.CTkLabel(self, text="Min Voltage")
        self.MinLabel.grid(row=0, column=1, padx=10, pady=(10, 0), sticky="nw")
        self.MinBox = customtkinter.CTkEntry(self, placeholder_text="Min")
        self.MinBox.grid(row=1, column=1, padx=10, pady=0, sticky="nw")
        self.MaxLabel = customtkinter.CTkLabel(self, text="Max Voltage")
        self.MaxLabel.grid(row=2, column=1, padx=10, pady=(10, 0), sticky="nw")
        self.MaxBox = customtkinter.CTkEntry(self, placeholder_text="Max")
        self.MaxBox.grid(row=3, column=1, padx=10, pady=0, sticky="nw")
        
        self.CurveStepLabel = customtkinter.CTkLabel(self, text="Step Voltage")
        self.CurveStepLabel.grid(row=0, column=2, padx=10, pady=(10, 0), sticky="nw")
        self.CurveStepBox = customtkinter.CTkEntry(self, placeholder_text="StepV")
        self.CurveStepBox.grid(row=1, column=2, padx=10, pady=0, sticky="nw")
        self.PointsLabel = customtkinter.CTkLabel(self, text="Points Per Plot")
        self.PointsLabel.grid(row=2, column=2, padx=10, pady=(10, 0), sticky="nw")
        self.PointsBox = customtkinter.CTkEntry(self, placeholder_text="Points")
        self.PointsBox.grid(row=3, column=2, padx=10, pady=0, sticky="nw")
        
        self.TraceLabel = customtkinter.CTkLabel(self, text="Num Traces")
        self.TraceLabel.grid(row=0, column=3, padx=10, pady=(10, 0), sticky="nw")            
        self.TraceBox = customtkinter.CTkEntry(self, placeholder_text="Traces")
        self.TraceBox.grid(row=1, column=3, padx=10, pady=0, sticky="nw")
        self.PlotButtonLabel = customtkinter.CTkLabel(self, text=" ")
        self.PlotButtonLabel.grid(row=2, column=3, padx=10, pady=(10, 0), sticky="nw")          
        self.PlotButton = customtkinter.CTkButton(self, text="Plot", command=self.button_callback)
        self.PlotButton.grid(row=3, column=3, padx=10, pady=0, sticky="nw")
        
        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().grid(row=4, columnspan=4, pady=(20, 0), sticky="n")

    def button_callback(self):
        print("button pressed")




app = App()
ani = animation.FuncAnimation(f, animate, interval=1000, cache_frame_data=False)
app.mainloop()
