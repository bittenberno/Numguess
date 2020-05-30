from cx_Freeze import setup, Executable

setup(name = "ping_bot" ,
      version = "1.0.0" ,
      description = "pingt im angegebenen Radius und gibt das Ergebnis in eienr liste aus." ,
      executables = [Executable("Zahlenraten_1_0_2.py")])