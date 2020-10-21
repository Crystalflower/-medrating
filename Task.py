import json
import datetime

with open("todos.json") as read_f:
    data = json.load(read_f)

data = [el for el in data if el.keys() == {'userId', 'id', 'title', 'completed'}]

count = {el.get('userId') for el in data}

today = datetime.datetime.today()


class Worker:

    def __init__(self, num, information):
        self.number = num
        self.tasks = information

    def get_completed_tasks(self):
        return (el.get('title') for el in self.tasks if el.get('completed') is True)

    def get_uncompleted_tasks(self):
        return (el.get('title') for el in self.tasks if el.get('completed') is False)

    def get_result(self, date):
        result = [f'# Сотрудник №{self.number}\n{date.strftime("%d.%m.%Y %H:%M")}\n', '\n## Завершенные задачи:\n']
        for task in self.get_completed_tasks():
            if len(task) <= 50:
                result.append(task + '\n')
            else:
                result.append(task[:50] + '...\n')
        result.append('\n## Оставшиеся задачи:\n')
        for task in self.get_uncompleted_tasks():
            if len(task) <= 50:
                result.append(task + '\n')
            else:
                result.append(task[:50] + '...\n')
        return result


for i in count:
    with open(f'{i}_{today.strftime("%Y-%m-%dT%H-%M")}.txt', 'w', encoding='utf-8') as new_file:
        record = Worker(i, [el for el in data if el.get('userId') == i])
        new_file.writelines(record.get_result(today))
