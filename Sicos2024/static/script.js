const mobileScreen = window.matchMedia("(max-width: 990px )");
$(document).ready(function () {
    $(".dashboard-nav-dropdown-toggle").click(function () {
        $(this).closest(".dashboard-nav-dropdown")
            .toggleClass("show")
            .find(".dashboard-nav-dropdown")
            .removeClass("show");
        $(this).parent()
            .siblings()
            .removeClass("show");
    });
    $(".menu-toggle").click(function () {
        if (mobileScreen.matches) {
            $(".dashboard-nav").toggleClass("mobile-show");
        } else {
            $(".dashboard").toggleClass("dashboard-compact");
        }
    });
});


document.addEventListener('DOMContentLoaded', () => {
    const tablaClientes = document.getElementById('tabla-clientes');
    const tablaPolizas = document.getElementById('tabla-polizas');

    tablaClientes.addEventListener('click', (event) => {
        if (event.target.classList.contains('cliente-link')) {
            event.preventDefault();
            const idCliente = event.target.closest('tr').dataset.idcliente;

            fetch(`/obtener_polizas/${idCliente}/`)
                .then(response => response.json())
                .then(data => {
                    let tablaPolizasHTML = '<table class="table table-hover"><thead><tr><th>IdPoliza</th><th>Número de Póliza</th></tr></thead><tbody>';
                    data.polizas.forEach(poliza => {
                        tablaPolizasHTML += `<tr><td>${poliza.IdPoliza}</td><td>${poliza.NumeroPoliza}</td></tr>`;
                    });
                    tablaPolizasHTML += '</tbody></table>';
                    tablaPolizas.innerHTML = tablaPolizasHTML;
                });
        }
    });
});