document.addEventListener('DOMContentLoaded', () => {
  async function handleFormSubmit(event) {
    event.preventDefault();

    const form = event.target;
    const url = form.action;
    const csrfToken = form.querySelector('[name=csrfmiddlewaretoken]').value;
    const formData = new FormData(form);

    try {
      const response = await fetch(url, {
        method: 'POST',
        headers: {
          'X-CSRFToken': csrfToken,
        },
        body: formData,
      });

      const data = await response.json();
      const message = data.status === 'success' ? data.message : data.error;
      alert(message);
    } catch (error) {
      console.error('Error:', error);
      alert('Se produjo un error al procesar la solicitud.');
    }
  };

  const forms = document.querySelectorAll('.add-to-favorite, .add-to-versus');
  forms.forEach((form) => {
    form.addEventListener('submit', handleFormSubmit);
  });
});
