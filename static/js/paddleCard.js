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
      Swal.fire({
        title: 'Éxito!',
        text: message,
        icon: 'success',
        confirmButtonText: 'Cool'
      })
      
    } catch (error) {
      console.error('Error:', error);
      Swal.fire({
        title: 'Error!',
        text: 'Se produjo un error al procesar la solicitud.',
        icon: 'error',
        confirmButtonText: 'Cool'
      })
    }
  };

  const forms = document.querySelectorAll('.add-to-favorite, .add-to-versus');
  forms.forEach((form) => {
    form.addEventListener('submit', handleFormSubmit);
  });
});
