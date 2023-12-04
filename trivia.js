document.addEventListener('DOMContentLoaded', function() {
    // Correct answer:
    let correct = document.querySelector('.correct');
    correct.addEventListener('click', function() {
        correct.style.backgroundColor = 'green';
        document.querySelector('#feedback1').innerHTML = 'Correct!';
    });

    // Incorrect answer:
    let incorrect = document.querySelectorAll('.incorrect');
    for (let i = 0; i < incorrect.length; i++) {
        incorrect[i].addEventListener('click', function() {
            incorrect[i].style.backgroundColor = 'red';
            document.querySelector('#feedback1').innerHTML = 'Incorrect!';
        });
    }

    document.querySelector('#check').addEventListener('click', function() {
        let input = document.querySelector('input');
        if (input.value === 'Ravenclaw') {
            input.style.backgroundColor = 'green';
            document.querySelector('#feedback2').innerHTML = 'Correct!';
        } else {
            input.style.backgroundColor = 'red';
            document.querySelector('#feedback2').innerHTML = 'Incorrect!';
        }
    });
});
