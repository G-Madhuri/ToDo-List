from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory list to store tasks
tasks = []

def heapify(arr, n, i, key):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left][key] > arr[largest][key]:
        largest = left
    if right < n and arr[right][key] > arr[largest][key]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest, key)

def heap_sort(arr, key):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, key)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0, key)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        title = request.form['title']
        due_date = request.form['due_date']
        priority = request.form['priority']
        task_id = request.form.get('task_id', None)

        if task_id:  # Edit existing task
            tasks[int(task_id)] = {
                'title': title,
                'due_date': due_date,
                'priority': int(priority),
                'completed': tasks[int(task_id)]['completed']
            }
        else:  # Add new task
            tasks.append({
                'title': title,
                'due_date': due_date,
                'priority': int(priority),
                'completed': False
            })
        return redirect(url_for('index'))

    # Sorting and filtering
    filter_status = request.args.get('filter', 'all')
    filtered_tasks = [task for task in tasks if (filter_status == 'all' or
                                                  (filter_status == 'completed' and task['completed']) or
                                                  (filter_status == 'pending' and not task['completed']))]

    sort_by = request.args.get('sort', 'due_date')
    if sort_by == 'due_date':
        heap_sort(filtered_tasks, 'due_date')
    elif sort_by == 'priority':
        heap_sort(filtered_tasks, 'priority')

    return render_template('index.html', tasks=filtered_tasks)

@app.route('/complete/<int:task_id>')
def complete_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks[task_id]['completed'] = not tasks[task_id]['completed']
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    return redirect(url_for('index'))

@app.route('/edit/<int:task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    if request.method == 'POST':
        title = request.form['title']
        due_date = request.form['due_date']
        priority = request.form['priority']
        tasks[task_id] = {
            'title': title,
            'due_date': due_date,
            'priority': int(priority),
            'completed': tasks[task_id]['completed']
        }
        return redirect(url_for('index'))
    
    if 0 <= task_id < len(tasks):
        task_to_edit = tasks[task_id]
        return render_template('index.html', tasks=tasks, edit_task=task_to_edit, task_id=task_id)
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
