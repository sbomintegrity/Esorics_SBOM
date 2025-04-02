<?php
// Load tasks from JSON file
$dataFile = 'data.json';
$tasks = json_decode(file_get_contents($dataFile), true);

require __DIR__ . '/vendor/autoload.php';

use Monolog\Logger;
use Monolog\Handler\StreamHandler;

// Create a log channel
$log = new Logger('todo');
$log->pushHandler(new StreamHandler(__DIR__.'/app.log', Logger::INFO));

// Handle form submission
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (isset($_POST['task'])) {
        // Add new task
        $newTask = [
            'id' => time(),
            'task' => htmlspecialchars($_POST['task']),
            'completed' => false
        ];
        $tasks[] = $newTask;
        $log->info('New task added', ['task' => $newTask]);
    } elseif (isset($_POST['complete'])) {
        // Mark task as complete
        foreach ($tasks as &$task) {
            if ($task['id'] == $_POST['complete']) {
                $task['completed'] = !$task['completed'];
                $log->info('Task completion toggled', ['task' => $task]);
            }
        }
    } elseif (isset($_POST['delete'])) {
        // Delete task
        $tasks = array_filter($tasks, fn($task) => $task['id'] != $_POST['delete']);
        $log->info('Task deleted', ['task_id' => $_POST['delete']]);
    }

    // Save changes
    file_put_contents($dataFile, json_encode(array_values($tasks), JSON_PRETTY_PRINT));
    header('Location: index.php');
    exit;
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>PHP To-Do App</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <h2>PHP To-Do List</h2>
    
    <form method="POST">
        <input type="text" name="task" placeholder="Enter new task" required>
        <button type="submit">Add Task</button>
    </form>

    <ul>
        <?php foreach ($tasks as $task): ?>
            <li class="<?= $task['completed'] ? 'completed' : '' ?>">
                <?= htmlspecialchars($task['task']) ?>

                <form method="POST" style="display:inline;">
                    <button name="complete" value="<?= $task['id'] ?>">
                        <?= $task['completed'] ? 'Undo' : 'Complete' ?>
                    </button>
                </form>

                <form method="POST" style="display:inline;">
                    <button name="delete" value="<?= $task['id'] ?>">Delete</button>
                </form>
            </li>
        <?php endforeach; ?>
    </ul>
</body>
</html>
