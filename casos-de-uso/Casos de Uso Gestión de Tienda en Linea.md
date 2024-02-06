# Casos de Uso Reserva de vuelo

## Descripcion:
Diseña un diagrama de casos de uso para un sistema de gestión de tienda en línea. Los actores pueden ser "Cliente" y "Administrador". Casos de uso incluyen: **Ver Catálogo", "Realizar Compra", "Gestionar Inventario.**

## Casos de Uso:
1. **Ver Catálogo en Línea:** El cliente puede ver los productos disponibles en la tienda en línea. El administrador puede agregar, eliminar o actualizar productos en el catálogo.

2. **Realizar Compra:** El cliente puede comprar un producto seleccionado. El cliente debe proporcionar información personal, como el nombre, la dirección, el número de teléfono, etc. El cliente también debe proporcionar información de pago, como el número de tarjeta de crédito, la fecha de vencimiento, el código de seguridad, etc. El administrador debe actualizar el inventario después de que se realize una compra.
 
3. **Gestionar Inventario:** El administrador puede agregar, eliminar o actualizar productos en el catálogo. El administrador también debe actualizar el inventario después de que se realiza una compra.

| **Actor**       | **Usuario**                          |
|-------------|------------------------------------------------|
| **Descripción** | El usuario puede logearse en la pagina web para adquirir articulos                     |
| **Características** | La web recibe los pedidos del usuario y los precesa      |
| **Referencias** | Ver Catálogo en Línea, Realizar Compra                    |
| **Autor**       | Usuario   |



| **Caso de Uso** | **Administrador** |
|----------------|-----|
| **Fuentes**        | Documento que sustenta el caso de uso |
| **Actor**          | Actores que participan en el caso de uso |
| **Descripción**    |El administrador gestiona los pedidos de la pagina web de la tienda|
| **Flujo básico**   | La pagina web recibe el pedido del usuario, el adimnistrador ve el numero del pedido y lo que el usuario desea y comprueba la disponibilidad de los productos, actualizando los mismos segun los productos reclamados ademas de poner para su procesado los productos del usuario, una vez terminados los productos y o empaquetados, el administrador pone a disposicion de los transportistas el pedido |
| **Pre-condiciones**  | Se verifica la disponibilidad de los productos |
| **Post-condiciones**  | Se procesa el envio de los productos al usuario |
| **Requisitos**     | El usuario debe disponer de dinero en su tarjeta de credito |
| **Casos excepcionales**          | El usuario no didpone de dinero suficiente en su tarjeta por lo que se produce un error de pago, la tienda no dispone de los productos que el usuario desea o esteos estan agotados |
| **Autor**          | administrador |