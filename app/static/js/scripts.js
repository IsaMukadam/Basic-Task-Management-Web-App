document.addEventListener('DOMContentLoaded', fetchTasks);

const form = document.getElementById('task-form');
form.addEventListener('submit', async function(event) {
    event.preventDefault();
    const input = document.getElementById('task-input');
    const taskName = input.value;

    const response = await fetch('/tasks', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ task: taskName })
    });

    if (response.ok) {
        input.value = ''; // Clear the input field
        fetchTasks(); // Fetch the updated task list
    }
});

async function fetchTasks() {
    const response = await fetch('/tasks');
    const tasks = await response.json();
    const taskList = document.getElementById('task-list').querySelector('ul');
    taskList.innerHTML = ''; // Clear the current list

    tasks.forEach(task => {
        const li = document.createElement('li');
        li.classList.add('task-box');
        li.textContent = task.name;
        taskList.appendChild(li);
    });
}
