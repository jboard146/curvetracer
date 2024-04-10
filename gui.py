import customtkinter
#from customtkinter import ttk
import matplotlib
matplotlib.use("TKAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.animation as animation
from matplotlib.figure import Figure
from matplotlib import style
import curvetracer


style.use('seaborn-v0_8-whitegrid')

f = Figure(figsize=(20,20), dpi=150, layout='tight')
a = f.add_subplot(111)


myMeasurement = curvetracer.Measurement()
myMeasurement.setType('NPN') #Set a Default Value to Populate OptionList

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

    print('tick')
    
    a.clear()
    a.plot(xList, yList)
    a.set(xlabel="V", ylabel="V")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Curve Tracer")
        self.geometry("800x600")
        self.grid_columnconfigure(4, weight=1)
        self.grid_rowconfigure(5, weight=1)
        self.measureOptionList = myMeasurement.getMeasureTypeList()
        self.measureTypeOptionList = myMeasurement.getDeviceTypeList()
        self.selectedMeasureOption = customtkinter.StringVar(value=self.measureOptionList[0])
        self.selectedTypeOption = customtkinter.StringVar(value=self.measureTypeOptionList[1])
        
        
        # Col 0
        self.deviceLabel = customtkinter.CTkLabel(self, text="Device Type")
        self.deviceLabel.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nw")
        self.deviceOption = customtkinter.CTkOptionMenu(self, variable=self.selectedTypeOption, values=myMeasurement.getDeviceTypeList(), command=self.setDeviceOption) # Need to get list
        #self.deviceOption.set(self.selectedTypeOption)
        self.deviceOption.grid(row=1, column=0, padx=10, pady=0, sticky="nw")
        self.measureLabel = customtkinter.CTkLabel(self, text="Measurement")
        self.measureLabel.grid(row=2, column=0, padx=10, pady=(10, 0), sticky="nw")
        self.measureOption = customtkinter.CTkOptionMenu(self, variable=self.selectedMeasureOption, values=myMeasurement.getMeasureTypeList(), command=self.setMeasurementOption) # Need to get list  
        #self.measureOption.set(self.selectedMeasureOption)
        self.measureOption.grid(row=3, column=0, padx=10, pady=0, sticky="nw")

        # Col 1
        self.R1Label = customtkinter.CTkLabel(self, text="Rb/Rg")
        self.R1Label.grid(row=0, column=1, padx=10, pady=(10, 0), sticky="nw")
        self.R1Box = customtkinter.CTkEntry(self, placeholder_text="Rb/Rg")
        self.R1Box.grid(row=1, column=1, padx=10, pady=0, sticky="nw")
        self.R2Label = customtkinter.CTkLabel(self, text="Rc/Rs")
        self.R2Label.grid(row=2, column=1, padx=10, pady=(10, 0), sticky="nw")
        self.R2Box = customtkinter.CTkEntry(self, placeholder_text="Rc/Rs")
        self.R2Box.grid(row=3, column=1, padx=10, pady=0, sticky="nw")
        
        # Col 2
        self.MinLabel = customtkinter.CTkLabel(self, text="Min Voltage")
        self.MinLabel.grid(row=0, column=2, padx=10, pady=(10, 0), sticky="nw")
        self.MinBox = customtkinter.CTkEntry(self, placeholder_text="Min")
        self.MinBox.grid(row=1, column=2, padx=10, pady=0, sticky="nw")
        self.MaxLabel = customtkinter.CTkLabel(self, text="Max Voltage")
        self.MaxLabel.grid(row=2, column=2, padx=10, pady=(10, 0), sticky="nw")
        self.MaxBox = customtkinter.CTkEntry(self, placeholder_text="Max")
        self.MaxBox.grid(row=3, column=2, padx=10, pady=0, sticky="nw")
        
        # Col 3
        self.CurveStepLabel = customtkinter.CTkLabel(self, text="Step Voltage")
        self.CurveStepLabel.grid(row=0, column=2, padx=10, pady=(10, 0), sticky="nw")
        self.CurveStepBox = customtkinter.CTkEntry(self, placeholder_text="StepV")
        self.CurveStepBox.grid(row=1, column=2, padx=10, pady=0, sticky="nw")
        self.PointsLabel = customtkinter.CTkLabel(self, text="Points Per Plot")
        self.PointsLabel.grid(row=2, column=3, padx=10, pady=(10, 0), sticky="nw")
        self.PointsBox = customtkinter.CTkEntry(self, placeholder_text="Points")
        self.PointsBox.grid(row=3, column=3, padx=10, pady=0, sticky="nw")
        
        # Col 4
        self.TraceLabel = customtkinter.CTkLabel(self, text="Num Traces")
        self.TraceLabel.grid(row=0, column=4, padx=10, pady=(10, 0), sticky="nw")            
        self.TraceBox = customtkinter.CTkEntry(self, placeholder_text="Traces")
        self.TraceBox.grid(row=1, column=4, padx=10, pady=0, sticky="nw")
        
        
        # Row 5 & 6 Buttons
        self.PlotButtonLabel = customtkinter.CTkLabel(self, text=" ")
        self.PlotButtonLabel.grid(row=5, column=0, padx=10, pady=(10, 0), sticky="nw")          
        self.PlotButton = customtkinter.CTkButton(self, text="Plot", command=self.plot_button_callback)
        self.PlotButton.grid(row=6, column=0, padx=10, pady=0, sticky="nw")
        self.SaveTraceButtonLabel = customtkinter.CTkLabel(self, text=" ")
        self.SaveTraceButtonLabel.grid(row=5, column=1, padx=10, pady=(10, 0), sticky="nw") 
        self.SaveTraceButton = customtkinter.CTkButton(self, text="Save", command=self.save_button_callback)
        self.SaveTraceButton.grid(row=6, column=1, padx=10, pady=(10, 0), sticky="nw")
        
        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().grid(row=4, columnspan=4, pady=(20, 0), sticky="n")

    def setDeviceOption(self, s_Val):
        
        myMeasurement.setType(s_Val)
        
        self.selectedTypeOption = s_Val
        
        # Update Mesaurement List
        self.measureOptionList = myMeasurement.getMeasureTypeList()
        # Set default option variable and value to the first element since we are updating the drvice type
        self.selectedMeasureOption = self.measureOptionList[0]
        # Update Gui Measurement List
        self.measureOption.configure(values=self.measureOptionList)
        # Updated selected default GUI Value
        self.measureOption.set(self.selectedMeasureOption)
        
        #print("Device Option: ", s_Val)
    
    def setMeasurementOption(self, s_Val):     
        # Update mesaurement option value
        self.selectedMeasureOption = s_Val
        #print("Measurement Option: ", s_Val)
    
    def plot_button_callback(self):
        print("Plot Button Pressed")
        
    def save_button_callback(self):
        print("Save Trace Button Presssed")
        
    




app = App()
ani = animation.FuncAnimation(f, animate, interval=5000, cache_frame_data=False)
app.mainloop()
