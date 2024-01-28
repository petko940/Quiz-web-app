document.addEventListener('DOMContentLoaded', function () {

    const quizOptions = document.getElementsByClassName('option');
    const rightAnswer = document.getElementsByClassName('right-answer')[0];
    let optionSelected = false;
    let ifWrong = false;

    Array.from(quizOptions).forEach((option) => {
        option.addEventListener('click', async () => {
            if (optionSelected) {
                return;
            }

            option.style.backgroundColor = 'orange';

            Array.from(quizOptions).forEach((option) => {
                option.style.cursor = 'default';
            })
            optionSelected = true;

            setTimeout(() => {
                if (option.textContent === rightAnswer.textContent) {
                    option.style.backgroundColor = 'green';
                } else {
                    option.style.backgroundColor = 'red';
                    ifWrong = true;
                }

                Array.from(quizOptions).forEach((option) => {
                    if (ifWrong) {
                        setTimeout(() => {
                            if (option.textContent === rightAnswer.textContent) {
                                option.style.backgroundColor = 'green';
                            }
                        }, 1000);
                    }
                })
                
                const section = document.querySelector('section');
                const h1 = this.createElement('h1');
                h1.textContent = 'Just a joke. Redirecting to home page...';
                h1.setAttribute('class', 'text-3xl text-white text-center mt-10');
                section.appendChild(h1);
            
            }, 1000);
            setTimeout(() => {
                window.location.href = '/';
            }, 6500);
        })



    })


});