# task_to_ics 
**Problem Statement:** A need I have had multiple times while planning my work and schedule is a way in which I can list out the tasks I need to complete and provide an estimate of duration for each task and then get my digital calendar automatically populated with events to complete these tasks.  I used to write down my To-Do list on a spreadsheet and then manually create events on my calendar for the tasks. Friends suggested some paid services that could do something like this and some free services that let me create To-Do lists and provide motivation to finish the To-Do lists. But I could not find a free service that would ask me what my tasks are create a calendar for me.

**Solution:** This Python code solves the above problem. It asks user to input tasks one after another and then creates an .ics (calendar file) file that I can now import into my digital calendar.

**Future Expansion:** The current solution is minimal . I might in future extend this program to first import user supplied calendar and then create tasks around the existing calendar. Currently, I have to adjust task times for task that may be clashing with existing events on my calendar before import. 

**Repository Contents:** This repository has both the sourcecode in Python (iCalCreate.py) and the executable file. The .exe file that can be copied to run the program locally is iCalCreate.exe The rest are files generated while creating an .exe from the .py file using pyinstaller


