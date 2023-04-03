from collections import defaultdict

class TimedScheduler:
    """A class for scheduling tasks with dependencies.

    The TimedScheduler class schedules tasks by computing their start times based
    on their duration and the durations of their dependencies.

    Attributes:
        tasks (set): a set of all tasks to be scheduled
        predecessors (defaultdict): a dictionary of sets of tasks that are predecessors to each task
        successors (defaultdict): a dictionary of sets of tasks that are successors to each task
        sorted_tasks (list): a sorted list of tasks in order of increasing start time
    """

    def __init__(self):
        self.tasks = set()
        self.predecessors = defaultdict(set)
        self.successors = defaultdict(set)
        self.sorted_tasks = None

    def add_task(self, task, dependencies):
        """Add a task with given dependencies to the scheduler."""
        # Add the task and its dependencies to the set of tasks.
        self.tasks.add(task)
        self.tasks.update(dependencies)
        # Add the dependencies to the predecessors of the task.
        self.predecessors[task] = self.predecessors[task] | set(dependencies)
        for dependency in dependencies:
            self.successors[dependency].add(task)

    def compute_schedule(self):
        """Compute a schedule for the tasks in the scheduler."""
        # Initialization step: set the start time of each task to be negative its duration.
        for task in self.tasks:
            task.start_time = -task.duration

        # Iterations: update the start times of each task based on the start times of its successors.
        # If the graph contains a cycle, raise an exception.
        for num_iteration in range(len(self.tasks)):
            changed = False
            for task in self.tasks:
                new_time = -task.duration + min([0.] + [successor.start_time
                                                       for successor in self.successors[task]])
                changed = changed or new_time != task.start_time
                task.start_time = new_time
            if not changed:
                break
        else:
            # If we exit the loop normally, then we never found a fixed point, which means
            # the graph contains a cycle.
            raise ValueError("The graph contains a cycle.")

        # Sort the tasks by their start time.
        self.sorted_tasks = sorted(self.tasks, key=lambda task: task.start_time)

    def get_schedule(self):
        """Return the sorted list of tasks in order of increasing start time."""
        return self.sorted_tasks
    

'''
    The TimedScheduler class can be useful in scenarios where you want to schedule tasks to run at specific times or intervals. It allows you to add tasks with a specific delay or schedule tasks to run periodically at a certain interval.

For example, if you're building a program that needs to run certain tasks at specific times, such as sending an email reminder every day at a certain time, you could use the TimedScheduler class to schedule those tasks to run automatically.

Another scenario where this class could be useful is in simulations or games where you need to schedule events to happen at specific times or intervals. You could use the TimedScheduler class to schedule those events to happen at the appropriate times.

In summary, the TimedScheduler class can be used in any situation where you need to schedule tasks to run at specific times or intervals.

'''

