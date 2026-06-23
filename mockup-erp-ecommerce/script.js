const products = [
    { id: 1, name: "Mesa de Comedor", description: "Mesa de madera de roble para 6 personas", price: 4500, stock: 5, sku: "MUE-001", category: "Comedor", image: "🪑" },
    { id: 2, name: "Silla de Oficina", description: "Silla ergonómica de madera y cuero", price: 1200, stock: 15, sku: "MUE-002", category: "Oficina", image: "💺" },
    { id: 3, name: "Estantería", description: "Estantería de 5 niveles en madera de pino", price: 2800, stock: 8, sku: "MUE-003", category: "Almacenamiento", image: "📚" },
    { id: 4, name: "Cama King Size", description: "Cama de madera de caoba con base", price: 8500, stock: 3, sku: "MUE-004", category: "Dormitorio", image: "🛏️" },
    { id: 5, name: "Escritorio", description: "Escritorio moderno con cajones", price: 3200, stock: 10, sku: "MUE-005", category: "Oficina", image: "🖥️" },
    { id: 6, name: "Sillón", description: "Sillón tapizado de madera", price: 2500, stock: 7, sku: "MUE-006", category: "Sala", image: "🛋️" }
];

const orders = [
    { id: 1, number: "PED-001", customer: "María López", date: "2026-06-20", total: 5700, status: "PAGADO", isEcommerce: true, items: [{ product: "Mesa de Comedor", qty: 1, price: 4500 }, { product: "Silla de Oficina", qty: 1, price: 1200 }] },
    { id: 2, number: "PED-002", customer: "Juan Pérez", date: "2026-06-21", total: 4500, status: "PENDIENTE", isEcommerce: false, items: [{ product: "Mesa de Comedor", qty: 1, price: 4500 }] },
    { id: 3, number: "PED-003", customer: "Ana García", date: "2026-06-22", total: 1200, status: "ENVIADO", isEcommerce: true, items: [{ product: "Silla de Oficina", qty: 1, price: 1200 }] }
];

const productionOrders = [
    { id: 1, number: "OP-001", product: "Mesa de Comedor", quantity: 2, date: "2026-06-20", status: "EN_PRODUCCION", stage: "Ensamblado", history: ["Corte", "Ensamblado"] },
    { id: 2, number: "OP-002", product: "Cama King Size", quantity: 1, date: "2026-06-21", status: "PENDIENTE", stage: "Pendiente", history: [] },
    { id: 3, number: "OP-003", product: "Silla de Oficina", quantity: 5, date: "2026-06-19", status: "TERMINADA", stage: "Terminada", history: ["Corte", "Ensamblado", "Lijado", "Pintura", "Empaque", "Terminada"] }
];

const stages = ["Corte", "Ensamblado", "Lijado", "Pintura", "Empaque", "Terminada"];
const orderStatuses = ["PENDIENTE", "PAGADO", "ENVIADO", "ENTREGADO"];

let cart = [];
let nextProductId = 7;
let nextOrderId = 4;
let nextProductionId = 4;
let isEditing = false;

document.addEventListener('DOMContentLoaded', () => {
    renderProductGrid();
    renderProductsTable();
    renderOrdersTable();
    renderProductionTable();
    renderProductSelect();
    setupNavigation();
});

function setupNavigation() {
    const navButtons = document.querySelectorAll('.nav-btn');
    const sections = document.querySelectorAll('.section');

    navButtons.forEach(btn => {
        btn.addEventListener('click', () => {
            const targetSection = btn.dataset.section;
            
            navButtons.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            
            sections.forEach(s => s.classList.remove('active'));
            document.getElementById(targetSection).classList.add('active');
        });
    });
}

function renderProductGrid() {
    const grid = document.getElementById('productGrid');
    grid.innerHTML = products.map(product => `
        <div class="product-card">
            <div class="product-image">${product.image}</div>
            <div class="product-info">
                <h3>${product.name}</h3>
                <p>${product.description}</p>
                <div class="product-footer">
                    <span class="product-price">$${product.price.toFixed(2)}</span>
                    <button class="btn-primary" onclick="addToCart(${product.id})">Agregar</button>
                </div>
            </div>
        </div>
    `).join('');
}

function addToCart(productId) {
    const product = products.find(p => p.id === productId);
    if (!product) return;

    const existingItem = cart.find(item => item.id === productId);
    
    if (existingItem) {
        existingItem.quantity++;
    } else {
        cart.push({ ...product, quantity: 1 });
    }
    
    updateCartSummary();
    showNotification(`${product.name} agregado al carrito`, 'success');
}

function updateCartSummary() {
    const cartCount = document.getElementById('cartCount');
    const cartItems = document.getElementById('cartItems');
    const cartTotal = document.getElementById('cartTotal');
    
    const totalItems = cart.reduce((sum, item) => sum + item.quantity, 0);
    const totalPrice = cart.reduce((sum, item) => sum + (item.price * item.quantity), 0);
    
    cartCount.textContent = totalItems;
    cartTotal.textContent = totalPrice.toFixed(2);
    
    cartItems.innerHTML = cart.length > 0 
        ? cart.map(item => `
            <li>
                <span>${item.name} x${item.quantity}</span>
                <span>$${(item.price * item.quantity).toFixed(2)}</span>
            </li>
        `).join('')
        : '<li style="text-align: center; color: #636e72;">Carrito vacío</li>';
}

function checkout() {
    if (cart.length === 0) {
        showNotification('El carrito está vacío', 'warning');
        return;
    }
    
    const total = cart.reduce((sum, item) => sum + (item.price * item.quantity), 0);
    const newOrder = {
        id: nextOrderId++,
        number: `PED-${String(nextOrderId).padStart(3, '0')}`,
        customer: "Cliente Online",
        date: new Date().toISOString().split('T')[0],
        total: total,
        status: "PENDIENTE",
        isEcommerce: true,
        items: cart.map(item => ({ product: item.name, qty: item.quantity, price: item.price }))
    };
    
    orders.unshift(newOrder);
    cart = [];
    updateCartSummary();
    renderOrdersTable();
    showNotification('¡Compra realizada con éxito!', 'success');
}

function renderProductsTable() {
    const tbody = document.getElementById('productsTableBody');
    tbody.innerHTML = products.map(product => `
        <tr>
            <td>${product.sku}</td>
            <td>${product.name}</td>
            <td>${product.category}</td>
            <td>$${product.price.toFixed(2)}</td>
            <td>${product.stock}</td>
            <td>
                <button class="btn-action" onclick="editProduct(${product.id})">Editar</button>
                <button class="btn-action btn-action-danger" onclick="deleteProduct(${product.id})">Eliminar</button>
            </td>
        </tr>
    `).join('');
}

function editProduct(id) {
    const product = products.find(p => p.id === id);
    if (!product) return;
    
    isEditing = true;
    document.getElementById('productModalTitle').textContent = 'Editar Producto';
    document.getElementById('productId').value = product.id;
    document.getElementById('productName').value = product.name;
    document.getElementById('productCategory').value = product.category;
    document.getElementById('productPrice').value = product.price;
    document.getElementById('productStock').value = product.stock;
    document.getElementById('productDescription').value = product.description || '';
    
    openModal('productModal');
}

function deleteProduct(id) {
    const productIndex = products.findIndex(p => p.id === id);
    if (productIndex === -1) return;
    
    const productName = products[productIndex].name;
    products.splice(productIndex, 1);
    renderProductsTable();
    renderProductGrid();
    renderProductSelect();
    showNotification(`${productName} eliminado`, 'success');
}

function saveProduct() {
    const productId = document.getElementById('productId').value;
    
    if (isEditing && productId) {
        const productIndex = products.findIndex(p => p.id === parseInt(productId));
        if (productIndex !== -1) {
            products[productIndex].name = document.getElementById('productName').value;
            products[productIndex].category = document.getElementById('productCategory').value;
            products[productIndex].price = parseFloat(document.getElementById('productPrice').value);
            products[productIndex].stock = parseInt(document.getElementById('productStock').value);
            products[productIndex].description = document.getElementById('productDescription').value;
            
            showNotification('Producto actualizado exitosamente', 'success');
        }
    } else {
        const newProduct = {
            id: nextProductId++,
            name: document.getElementById('productName').value,
            category: document.getElementById('productCategory').value,
            price: parseFloat(document.getElementById('productPrice').value),
            stock: parseInt(document.getElementById('productStock').value),
            description: document.getElementById('productDescription').value,
            sku: `MUE-${String(nextProductId).padStart(3, '0')}`,
            image: "🪑"
        };
        
        products.push(newProduct);
        showNotification('Producto guardado exitosamente', 'success');
    }
    
    renderProductsTable();
    renderProductGrid();
    renderProductSelect();
    closeModal('productModal');
    resetProductForm();
}

function resetProductForm() {
    isEditing = false;
    document.getElementById('productModalTitle').textContent = 'Nuevo Producto';
    document.getElementById('productForm').reset();
    document.getElementById('productId').value = '';
}

function populateProductSelects() {
    const selects = document.querySelectorAll('.order-product-select');
    const options = '<option value="">Seleccionar producto</option>' + 
        products.map(p => `<option value="${p.id}">${p.name} ($${p.price.toFixed(2)})</option>`).join('');
    
    selects.forEach(select => {
        select.innerHTML = options;
    });
}

function openModal(modalId) {
    const modal = document.getElementById(modalId);
    if (modal) {
        if (modalId === 'productModal' && !isEditing) {
            resetProductForm();
        }
        if (modalId === 'newOrderModal') {
            // Resetear formulario
            document.getElementById('newOrderForm').reset();
            populateProductSelects();
            // Limpiar items extra (dejar solo 1)
            const container = document.getElementById('orderItemsContainer');
            const items = container.querySelectorAll('.order-item-row');
            for (let i = 1; i < items.length; i++) {
                items[i].remove();
            }
        }
        modal.classList.add('active');
    }
}

function addOrderItem() {
    const container = document.getElementById('orderItemsContainer');
    const template = container.querySelector('.order-item-row');
    const newItem = template.cloneNode(true);
    // Resetear valores
    newItem.querySelector('.order-product-select').value = '';
    newItem.querySelector('.order-item-qty').value = '1';
    container.appendChild(newItem);
    populateProductSelects();
}

function removeOrderItem(btn) {
    const container = document.getElementById('orderItemsContainer');
    const items = container.querySelectorAll('.order-item-row');
    if (items.length > 1) {
        btn.closest('.order-item-row').remove();
    } else {
        showNotification('Debe haber al menos un producto', 'warning');
    }
}

function saveNewOrder() {
    const customer = document.getElementById('orderCustomer').value;
    const isEcommerce = document.getElementById('orderOrigin').value === 'true';
    const itemRows = document.querySelectorAll('.order-item-row');
    
    if (!customer) {
        showNotification('Ingrese el nombre del cliente', 'warning');
        return;
    }

    let total = 0;
    const items = [];
    
    for (const row of itemRows) {
        const productId = parseInt(row.querySelector('.order-product-select').value);
        const qty = parseInt(row.querySelector('.order-item-qty').value);
        
        if (!productId) {
            showNotification('Seleccione un producto en todas las filas', 'warning');
            return;
        }
        
        const product = products.find(p => p.id === productId);
        if (!product) continue;
        
        const itemTotal = product.price * qty;
        total += itemTotal;
        items.push({
            product: product.name,
            qty: qty,
            price: product.price
        });
    }

    const newOrder = {
        id: nextOrderId++,
        number: `PED-${String(nextOrderId).padStart(3, '0')}`,
        customer: customer,
        date: new Date().toISOString().split('T')[0],
        total: total,
        status: 'PENDIENTE',
        isEcommerce: isEcommerce,
        items: items
    };
    
    orders.unshift(newOrder);
    renderOrdersTable();
    closeModal('newOrderModal');
    showNotification('Pedido creado exitosamente!', 'success');
}

function closeModal(modalId) {
    const modal = document.getElementById(modalId);
    if (modal) {
        modal.classList.remove('active');
    }
}

function renderOrdersTable() {
    const tbody = document.getElementById('ordersTableBody');
    tbody.innerHTML = orders.map(order => `
        <tr>
            <td>${order.number}</td>
            <td>${order.customer}</td>
            <td>${order.date}</td>
            <td>$${order.total.toFixed(2)}</td>
            <td><span class="status status-${order.status.toLowerCase()}">${order.status}</span></td>
            <td>${order.isEcommerce ? 'Online' : 'Presencial'}</td>
            <td>
                <button class="btn-action" onclick="viewOrder(${order.id})">Ver</button>
                <button class="btn-action" onclick="updateOrderStatus(${order.id})">Cambiar Estado</button>
            </td>
        </tr>
    `).join('');
}

function viewOrder(id) {
    const order = orders.find(o => o.id === id);
    if (!order) return;

    document.getElementById('orderModalTitle').textContent = `Pedido ${order.number}`;
    document.getElementById('orderModalBody').innerHTML = `
        <div class="detail-item">
            <div class="detail-label">Cliente</div>
            <div class="detail-value">${order.customer}</div>
        </div>
        <div class="detail-item">
            <div class="detail-label">Fecha</div>
            <div class="detail-value">${order.date}</div>
        </div>
        <div class="detail-item">
            <div class="detail-label">Origen</div>
            <div class="detail-value">${order.isEcommerce ? 'Online' : 'Presencial'}</div>
        </div>
        <div class="detail-item">
            <div class="detail-label">Estado</div>
            <div class="detail-value"><span class="status status-${order.status.toLowerCase()}">${order.status}</span></div>
        </div>
        <div class="detail-item">
            <div class="detail-label">Productos</div>
            <div class="detail-value">
                ${order.items.map(item => `
                    <div style="padding: 4px 0;">- ${item.product} x${item.qty} ($${item.price.toFixed(2)})</div>
                `).join('')}
            </div>
        </div>
        <div class="detail-item">
            <div class="detail-label">Total</div>
            <div class="detail-value" style="font-weight: 700; font-size: 20px; color: #27ae60;">$${order.total.toFixed(2)}</div>
        </div>
    `;
    openModal('orderModal');
}

function updateOrderStatus(id) {
    const order = orders.find(o => o.id === id);
    if (!order) return;
    
    const currentIndex = orderStatuses.indexOf(order.status);
    order.status = orderStatuses[(currentIndex + 1) % orderStatuses.length];
    
    renderOrdersTable();
    showNotification(`${order.number} ahora está: ${order.status}`, 'success');
}

function renderProductionTable() {
    const tbody = document.getElementById('productionTableBody');
    tbody.innerHTML = productionOrders.map(order => `
        <tr>
            <td>${order.number}</td>
            <td>${order.product}</td>
            <td>${order.quantity}</td>
            <td>${order.date}</td>
            <td><span class="status status-${order.status.toLowerCase().replace('_', '-')}">${order.status.replace('_', ' ')}</span></td>
            <td>${order.stage}</td>
            <td>
                <button class="btn-action" onclick="viewProduction(${order.id})">Ver</button>
                <button class="btn-action" onclick="advanceStage(${order.id})">Avanzar Etapa</button>
            </td>
        </tr>
    `).join('');
}

function viewProduction(id) {
    const order = productionOrders.find(o => o.id === id);
    if (!order) return;

    document.getElementById('productionDetailTitle').textContent = `Orden de Producción ${order.number}`;
    document.getElementById('productionDetailBody').innerHTML = `
        <div class="detail-item">
            <div class="detail-label">Producto</div>
            <div class="detail-value">${order.product}</div>
        </div>
        <div class="detail-item">
            <div class="detail-label">Cantidad</div>
            <div class="detail-value">${order.quantity} unidades</div>
        </div>
        <div class="detail-item">
            <div class="detail-label">Fecha de Creación</div>
            <div class="detail-value">${order.date}</div>
        </div>
        <div class="detail-item">
            <div class="detail-label">Estado</div>
            <div class="detail-value"><span class="status status-${order.status.toLowerCase().replace('_', '-')}">${order.status.replace('_', ' ')}</span></div>
        </div>
        <div class="detail-item">
            <div class="detail-label">Etapa Actual</div>
            <div class="detail-value">${order.stage}</div>
        </div>
        <div class="detail-item">
            <div class="detail-label">Historial de Etapas</div>
            <div class="detail-value">
                ${order.history.length > 0 ? order.history.map((stage, index) => `
                    <div style="padding: 4px 0;">
                        <span style="font-weight: 600;">${index + 1}.</span> ${stage}
                        ${index === order.history.length - 1 ? '<span style="color: #27ae60; margin-left: 8px;">✓ Actual</span>' : ''}
                    </div>
                `).join('') : '<div style="color: #636e72;">No hay etapas registradas</div>'}
            </div>
        </div>
    `;
    openModal('productionDetailModal');
}

function advanceStage(id) {
    const order = productionOrders.find(o => o.id === id);
    if (!order) return;
    
    if (order.status === "TERMINADA") {
        showNotification(`${order.number} ya está terminada`, 'warning');
        return;
    }
    
    const currentStageIndex = order.stage === "Pendiente" ? -1 : stages.indexOf(order.stage);
    
    if (currentStageIndex < stages.length - 1) {
        const nextStage = stages[currentStageIndex + 1];
        order.stage = nextStage;
        order.history.push(nextStage);
        
        if (nextStage === "Terminada") {
            order.status = "TERMINADA";
        } else {
            order.status = "EN_PRODUCCION";
        }
        
        renderProductionTable();
        showNotification(`${order.number} avanzó a: ${nextStage}`, 'success');
    }
}

function renderProductSelect() {
    const select = document.getElementById('productSelect');
    select.innerHTML = '<option value="">Seleccionar</option>' + 
        products.map(p => `<option value="${p.id}">${p.name}</option>`).join('');
}

function saveProduction() {
    const form = document.getElementById('productionForm');
    const inputs = form.querySelectorAll('.form-input');
    const productId = parseInt(inputs[0].value);
    const product = products.find(p => p.id === productId);
    
    if (!product) {
        showNotification('Seleccione un producto', 'warning');
        return;
    }
    
    const newOrder = {
        id: nextProductionId++,
        number: `OP-${String(nextProductionId).padStart(3, '0')}`,
        product: product.name,
        quantity: parseInt(inputs[1].value),
        date: new Date().toISOString().split('T')[0],
        status: "PENDIENTE",
        stage: "Pendiente",
        history: []
    };
    
    productionOrders.unshift(newOrder);
    renderProductionTable();
    closeModal('productionModal');
    form.reset();
    showNotification('Orden de producción creada', 'success');
}

function showNotification(message, type = 'info') {
    const notification = document.getElementById('notification');
    notification.textContent = message;
    notification.className = `notification ${type} active`;
    
    setTimeout(() => {
        notification.classList.remove('active');
    }, 3000);
}

document.querySelectorAll('.modal').forEach(modal => {
    modal.addEventListener('click', (e) => {
        if (e.target === modal) {
            modal.classList.remove('active');
        }
    });
});
