from database.database import Database
import json


class TaskService:
    def __init__(self, db_name: str | None = None):
        self.db = Database(db_name)

    def create(self, task: dict):
        self.db.execute_query(
            f"""insert into tasks (name, description) values ('{task["name"]}', '{task["description"]}')""",
        )
        return True

    def get_one(self, task_id: int):
        task = self.db.execute_query(f"""SELECT * FROM tasks WHERE id = {task_id}""")

        return task

    def get_many(self):
        results = self.db.execute_query("SELECT * FROM tasks")
        tasks = []
        # convertendo em dict
        for row in results:
            tasks.append(dict(row))

        return tasks

    def update(self, task_id: int, task: dict):
        query_parts = []

        if task.get("name") is not None:
            query_parts.append(f"""name = '{task['name']}'""")

        if task.get("description") is not None:
            query_parts.append(f"""description = '{task['description']}'""")

        if task.get("status") is not None:
            query_parts.append(f"""status = '{task['status']}'""")

        fields_update = ",".join(query_parts)

        query = f"""UPDATE tasks SET {fields_update}, updatedAt = CURRENT_TIMESTAMP where id= {task_id}"""

        self.db.execute_query(query)

    def delete(self, task_id: int):
        self.db.execute_query(f"""DELETE FROM tasks WHERE id = {task_id}""")

    def get_tasks_by_status(self, status: bool):
        tasks = self.db.execute_query(
            f"""SELECT * FROM tasks WHERE status = {status}"""
        )

        return tasks
