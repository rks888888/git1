#Simple program for calculating ENGINE CID
print ('What kind of calculation do you need to perform?')
print ('A - CID Calculation i.e. bore and stroke combination')
print ('B - Carb Calculation i.e. the best carb for the application')

ans= input('A or B')

if ans is 'A':

  print ('example bore x bore x stroke x number of cylinders x .7854 = CID')

  print ('Please input in Inches')

  cyl = input("How many cylinders is your engine: ")
  cylinders = int(cyl)
  strke = input("What is the stroke of your engine: ")
  stroke = float(strke)
  bor = input("What bore do you have:")
  bore = float(bor)
  engine = (bore * bore * stroke * cylinders * .7854)
  eng = str(engine)
  print ('The cubic inces of your block will be, ' + eng + ' thank you for your time.')

else:

  print ('Stock Engines Volumetric Efficency or VE = 0.85')
  print ('Mild Built Volumetric Efficency or VE = 0.90')
  print ('Racing Engines Volumetric Efficency or VE 1.0')

  EngCID = input("What CID is your engine:")
  EngineCID = int(EngCID)
  RPM = input ("What is the max RPM of your engine:")
  MXRPM = int(RPM)
  VolEff = input('What is your VE:')
  VE = float(VolEff)
  CarbCFM = ((EngineCID * MXRPM * VE) / 3456)
  carb = str(CarbCFM)
  print('The correct carburetor you will need ' + carb + ' cfm to function correctly')