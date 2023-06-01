import win32com.client

# Verbindung zum SAP GUI Scripting API herstellen
SapGuiAuto = win32com.client.GetObject("SAPGUI")
application = SapGuiAuto.GetScriptingEngine
connection = application.Children(0)
session = connection.Children(0)

# SAP GUI-Verbindungsinformationen anzeigen
print("Connected to SAP GUI.")
print("SAP System ID:", connection.SystemID)
print("SAP System Number:", connection.SystemNumber)
print("SAP Client:", connection.Client)
print("SAP User:", connection.User)

# SAP GUI-Verbindung trennen
session.findById("wnd[0]").sendVKey(0)