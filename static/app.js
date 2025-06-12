document.getElementById('workoutForm').addEventListener('submit', async function (e) {
    e.preventDefault();

    const form = e.target;
    const data = {
        date: form.date.value,
        exercise_name: form.exercise_name.value,
        set_order: parseInt(form.set_order.value),
        reps: parseInt(form.reps.value),
        weight: parseFloat(form.weight.value)
    };

    try {
        const res = await fetch('https://workout-tracker-s24m.onrender.com/workouts', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });

        const json = await res.json();
        document.getElementById('responseMessage').textContent = json.message || "Workout submitted!";
        form.reset();
    } catch (error) {
        document.getElementById('responseMessage').textContent = "Error submitting workout.";
        console.error(error);
    }
});
