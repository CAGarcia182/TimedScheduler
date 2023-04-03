# TimedScheduler

A class for scheduling tasks with dependencies.
    The TimedScheduler class schedules tasks by computing their start times based
    on their duration and the durations of their dependencies.
    Attributes:
        tasks (set): a set of all tasks to be scheduled
        predecessors (defaultdict): a dictionary of sets of tasks that are predecessors to each task
        successors (defaultdict): a dictionary of sets of tasks that are successors to each task
        sorted_tasks (list): a sorted list of tasks in order of increasing start time


  The TimedScheduler class can be useful in scenarios where you want to schedule tasks to run at specific times or intervals. 
  It allows you to add tasks with a specific delay or schedule tasks to run periodically at a certain interval.
  For example, if you're building a program that needs to run certain tasks at specific times, such as sending an email reminder 
  every day at a certain time, you could use the TimedScheduler class to schedule those tasks to run automatically.
  Another scenario where this class could be useful is in simulations or games where you need to schedule events to happen at 
  specific times or intervals. You could use the TimedScheduler class to schedule those events to happen at the appropriate times.
  In summary, the TimedScheduler class can be used in any situation where you need to schedule tasks to run at specific times or intervals.
