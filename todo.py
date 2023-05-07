import uuid
from typing import List, Optional, Dict, Union
from datetime import date, datetime, timedelta


def to_date(datestr):
    if datestr == "today":
        return date.today().isoformat()[:10]
    if datestr == "tomorrow":
        return (date.today() + timedelta(days=1)).isoformat()[:10]
    return datestr


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add(self, description: str, due: Optional[str] = None, priority: Optional[int] = None) -> Dict[str, Union[str, bool, int]]:
        task = {
            'id': str(uuid.uuid4()),
            'done': False,
            'description': description,
            'due': to_date(due),
            'priority': priority,
        }
        self.tasks.append(task)
        return task

    def update(self, task_id: str, done: Optional[bool] = None, description: Optional[str] = None,
               due: Optional[str] = None, priority: Optional[int] = None) -> Optional[Dict[str, Union[str, bool, int]]]:
        for task in self.tasks:
            if task['id'] == task_id:
                if done is not None:
                    task['done'] = done
                if description is not None:
                    task['description'] = description
                if due is not None:
                    task['due'] = to_date(due)
                if priority is not None:
                    task['priority'] = priority
                return task
        return None

    def delete(self, task_id: str) -> bool:
        for task in self.tasks:
            if task['id'] == task_id:
                self.tasks.remove(task)
                return True
        return False

    def get(self, done: Optional[bool] = None, priority: Optional[int] = None, sort: Optional[Union[str, List[str]]] = None) -> List[Dict[str, Union[str, bool, int]]]:
        filtered_tasks = self.tasks
        if done is not None:
            filtered_tasks = [task for task in filtered_tasks if task['done'] == done]
        if priority is not None:
            filtered_tasks = [task for task in filtered_tasks if task['priority'] == priority]

        if sort is not None:
            if isinstance(sort, str):
                sort = [sort]

            for criterion in reversed(sort):
                if criterion == 'due':
                    filtered_tasks.sort(key=lambda x: (x[criterion] if x[criterion] is not None else '3333-03-03'))
                elif criterion == 'priority':
                    filtered_tasks.sort(key=lambda x: (x[criterion] if x[criterion] is not None else float('inf')))
                elif criterion == 'done':
                    filtered_tasks.sort(key=lambda x: x[criterion])

        # Convert datetime.date objects to strings in the format 'YYYY-MM-DD' before returning
        return filtered_tasks
