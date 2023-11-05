# Anwendungspotenzial von LLMs in der ABAP-Entwicklung am Beispiel von ChatGPT

# Zusammenfassung
Diese Ausarbeitung zeigt dass ChatGPT nicht für die Codegenerierung in ABAP geeignet ist, es konnte nur 2.45% der 16400 Aufgaben lösen. Die Ergebnisse der Codegenerierung lassen sich durch Anpassungen der Parameter kaum verbessern. Wir vermuten das dies der Fall ist, da es zu wenig Trainingsdaten von ABAP-Code gibt. Die Version GPT-4 erzielte noch schlechtere Ergebnisse als die ältere Version GPT-3.5. ChatGPT eignet sich jedoch gut für Codeerklärungen und zum Verständnis von Code. Hier wurde der ABAP-Code in nahezu allen Testfällen korrekt erklärt. Weitere umfangreichere Tests sind erforderlich, um mehr Parameterkombinationen und deren Einfluss auf die Programmentwicklung zu untersuchen.

# Übersicht
In ```rfcMethod.py```:
- die Methode ```askChatGptForPromptsSingleThread``` kann anfragen an ChatGPT senden, hier können die Parameter genutzt werden um festzulegen welche Prompts mit wievielen Wiederholungen und mit welchen Varianten angefragt werden sollen, und wieviele Thread diese anfragen gleichzeitig senden sollen. Es wird eine JSON-Datei abgespeichert, die alle Antworten von ChatGPT enthält.
    
- die Methode ```runSavedFunctions``` durchläuft eine JSON-Datei mit Antworten von ChatGPT und führt diese auf dem ABAP Server aus. Hierfür werden erst mit der Funktion ```extractAbapFunctionInformation``` die Funktionsdetails aus dem Text extrahiert, dann wird über die PyRFC-Schnittstelle in ```pythonAbapInterface.createFunctionModule``` ein Funktionsbaustein auf dem ABAP-Server erstellt. Nun werden über ```testModule.check``` die angepassten Unit-Tests ausgeführt woraufhin der Funktionsbaustein mit ```pythonAbapInterface.deleteFunctionModule``` wieder gelöscht wird. Die Ergebnisse werden wieder in einer JSON-Datei zusammen mit den Antworten gespeichert.

Mit ```analyseTestResults.py``` können die Ergebnisse eines Testdurchlaufs analysiert werden. Hier wird unter anderem zusammengezählt wieviele Funktionen erfolgreich erstellt wurden, wieviele Unit-Tests erfolgreich durchlaufen wurden und welche Fehlermeldungen wie oft aufgetreten sind.

Mit ```runTests.py``` werden unsere Tests ausgeführt. Hierfür werden für jeden unserer automatisierten Tests die Parameter definiert, dann werden die Anfragen an ChatGPT gemacht, die Funktionen auf dem ABAP-Server ausprobiert und letztentlich die Ergebnisse analysiert. Diese Datei ist nicht dafür gedacht am Stück ausgeführt zu werden. Diese Schritte sollten nacheinander manuell ausgeführt werden und die Ergebnisse sollte überprüft werden um mögliche Fehler die durch die OpenAI-API oder den ABAP-Server entstehen zu finden. 

Der ```adjustedTests``` enthält unsere angepassten Unit-Tests, basierend auf denen von HumanEval.

Im Ordner ```abap_canonical_solutions``` befinden unsere selbsterstellten Musterlösungen zu den Prompts die wir in den manuellen Tests untersuchen.

Die Ordner: ```prompts```, ```prompts only text``` und ```prompts without examples``` enthalten die verschiedenen, auf HumanEval aufbauenden, Prompts die wir im Parameterfindungstest nutzen. Genauso enthalten die Ordner ```translated prompts``` und ```translated prompts without examples``` die auf deutsch übersetzten Prompts für den Test zur Unterscheidung der Ergebnisse in deutsch und englisch.

Die Ergebnisse dieser Ausarbeitung sind im Ordner ```results``` zu finden:
- Hier befinden sich für die automatischen Tests jeweils eine JSON-Datei pro Test. Diese enhalten sowohl alle Antworten von ChatGPT sowie die Zwischenschritte zur Funktionserstellung für jede Antwort als auch Ergebnisse jedes Unit-Tests zu jeder Antwort. 
- Für die manuelle Tests befinden sich hier sowohl manuell veränderten Prompts als auch sämtliche Antworten von ChatGPT. 

