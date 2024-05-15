const buttons = document.querySelectorAll('.card');
buttons.forEach(button => {
  button.addEventListener('click', () => {
    const id = button.dataset.id;
    const form = document.createElement('form');
    form.method = 'post';
    const input = document.createElement('input');
    input.type = 'hidden';
    input.name = 'id';
    input.value = id;
    form.appendChild(input);
    document.body.appendChild(form);
    form.submit();
  });
});