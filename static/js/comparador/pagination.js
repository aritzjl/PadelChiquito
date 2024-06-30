botonAplicar = document.getElementById('filtrosAplicar');
		botonAplicar.addEventListener('click', (e) => {
			e.preventDefault();
			input_pagina.value = 1;
			formularioPrincipal.submit();
		});
		formularioPrincipal = document.getElementById('filtersContainer');
		input_pagina = document.getElementById('pageNumber');
		paginacion = document.getElementById('paginationContainer');

		// Función para cambiar la página
		function cambiarPagina(pagina) {
			input_pagina.value = pagina;
			formularioPrincipal.submit();
		}

		// Evento para cambiar la página
		paginacion.addEventListener('click', (e) => {
			if (e.target.tagName === 'A') {
				cambiarPagina(e.target.dataset.page);
			}
		});
