# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 16:43:39 2025

@author: sbnidhir
"""
import os
import tkinter as tk
from tkinter import simpledialog, messagebox
from datetime import datetime, timedelta
from icalendar import Calendar, Event

def create_ics_file(tasks, start_date):
    cal = Calendar()
    current_time = datetime.strptime(start_date, "%Y-%m-%d %H:%M")
    
    for task, duration in tasks:
        remaining_time = duration
        while remaining_time > 0:
            event_duration = min(0.5, remaining_time)  # Each event is 30 mins (0.5 hours)
            event = Event()
            event.add('summary', task)
            event.add('dtstart', current_time)
            event.add('dtend', current_time + timedelta(hours=event_duration))
            event.add('dtstamp', datetime.now())
            cal.add_component(event)
            
            # Update current time for next event segment
            current_time += timedelta(hours=event_duration)
            remaining_time -= event_duration
    
    output_filename = f"SBNCal_{datetime.today().strftime('%Y-%m-%d')}.ics"
    output_path = os.path.join(os.getcwd(), output_filename)
    with open(output_path, 'wb') as f:
        f.write(cal.to_ical())
    
    messagebox.showinfo("Success", f"ICS file '{output_filename}' created successfully.")

def get_tasks_from_user():
    tasks = []
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    
    start_date = simpledialog.askstring("Input", "Enter start date and time (YYYY-MM-DD HH:MM) or press Cancel to use default date of tomorrow:")
    if not start_date:
        start_date = (datetime.today() + timedelta(days = 1)).strftime("%Y-%m-%d %H:%M") 
        messagebox.showinfo("Note", "Tomorrow's date used as no date given.")
        #return
    
    while True:
        task = simpledialog.askstring("Input", "Enter task name (or leave blank to finish):")
        if not task:
            break
        try:
            duration = float(simpledialog.askstring("Input", f"Enter duration in hours for '{task}':"))
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number for duration.")
            continue
        tasks.append((task, duration))
    
    if tasks:
        create_ics_file(tasks, start_date)

def main():
    get_tasks_from_user()

if __name__ == "__main__":
    main()

