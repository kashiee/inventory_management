const API_URL = 'http://localhost:8000';
let token = null;

document.addEventListener('DOMContentLoaded', () => {
  document.getElementById('year').textContent = new Date().getFullYear();

  // Navigation
  const navLogin = document.getElementById('nav-login');
  const navRegister = document.getElementById('nav-register');
  const navProducts = document.getElementById('nav-products');
  const navAdd = document.getElementById('nav-add');
  const navUpdate = document.getElementById('nav-update');
  const navLogout = document.getElementById('nav-logout');

  // Sections
  const loginForm = document.getElementById('login-form');
  const registerForm = document.getElementById('register-form');
  const productsList = document.getElementById('products-list');
  const addForm = document.getElementById('add-form');
  const updateForm = document.getElementById('update-form');
  const message = document.getElementById('message');

  function show(tab) {
    loginForm.style.display = tab === 'login' ? '' : 'none';
    registerForm.style.display = tab === 'register' ? '' : 'none';
    productsList.style.display = tab === 'products' ? '' : 'none';
    addForm.style.display = tab === 'add' ? '' : 'none';
    updateForm.style.display = tab === 'update' ? '' : 'none';
    message.style.display = 'none';
  }

  function setNav(auth) {
    navLogin.style.display = auth ? 'none' : '';
    navRegister.style.display = auth ? 'none' : '';
    navProducts.style.display = auth ? '' : 'none';
    navAdd.style.display = auth ? '' : 'none';
    navUpdate.style.display = auth ? '' : 'none';
    navLogout.style.display = auth ? '' : 'none';
  }

  function showMessage(msg) {
    message.textContent = msg;
    message.style.display = '';
  }

  // Navigation events
  navLogin.onclick = () => { show('login'); };
  navRegister.onclick = () => { show('register'); };
  navProducts.onclick = () => { show('products'); fetchProducts(); };
  navAdd.onclick = () => { show('add'); };
  navUpdate.onclick = () => { show('update'); };
  navLogout.onclick = () => {
    token = null;
    setNav(false);
    show('login');
    showMessage('Logged out.');
  };

  // Register
  registerForm.onsubmit = async e => {
    e.preventDefault();
    const username = document.getElementById('register-username').value;
    const password = document.getElementById('register-password').value;
    const res = await fetch(`${API_URL}/register`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ username, password })
    });
    if (res.ok) {
      show('login');
      showMessage('Registration successful! Please login.');
    } else {
      showMessage('Registration failed.');
    }
  };

  // Login
  loginForm.onsubmit = async e => {
    e.preventDefault();
    const username = document.getElementById('login-username').value;
    const password = document.getElementById('login-password').value;
    const form = new URLSearchParams();
    form.append('username', username);
    form.append('password', password);
    const res = await fetch(`${API_URL}/login`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
      body: form.toString()
    });
    if (res.ok) {
      const data = await res.json();
      token = data.access_token;
      setNav(true);
      show('products');
      fetchProducts();
      showMessage('Login successful!');
    } else {
      showMessage('Login failed.');
    }
  };

  // Fetch products
  async function fetchProducts() {
    if (!token) return;
    const res = await fetch(`${API_URL}/products`, {
      headers: { Authorization: `Bearer ${token}` }
    });
    if (res.ok) {
      const products = await res.json();
      renderProducts(products);
    } else {
      showMessage('Failed to fetch products.');
    }
  }

  function renderProducts(products) {
    let html = '<h2>Products</h2><table><thead><tr>' +
      '<th>ID</th><th>Name</th><th>Type</th><th>SKU</th><th>Image</th><th>Description</th><th>Quantity</th><th>Price</th></tr></thead><tbody>';
    for (const p of products) {
      html += `<tr><td>${p.id}</td><td>${p.name}</td><td>${p.type}</td><td>${p.sku}</td><td>${p.image_url ? `<img src="${p.image_url}" alt="${p.name}" />` : '-'}</td><td>${p.description || ''}</td><td>${p.quantity}</td><td>$${p.price.toFixed(2)}</td></tr>`;
    }
    html += '</tbody></table>';
    productsList.innerHTML = html;
  }

  // Add product
  addForm.onsubmit = async e => {
    e.preventDefault();
    const payload = {
      name: document.getElementById('add-name').value,
      type: document.getElementById('add-type').value,
      sku: document.getElementById('add-sku').value,
      image_url: document.getElementById('add-image').value,
      description: document.getElementById('add-desc').value,
      quantity: Number(document.getElementById('add-qty').value),
      price: Number(document.getElementById('add-price').value)
    };
    const res = await fetch(`${API_URL}/products`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${token}`
      },
      body: JSON.stringify(payload)
    });
    if (res.ok) {
      show('products');
      fetchProducts();
      showMessage('Product added!');
      addForm.reset();
    } else {
      showMessage('Failed to add product.');
    }
  };

  // Update quantity
  updateForm.onsubmit = async e => {
    e.preventDefault();
    const id = document.getElementById('update-id').value;
    const quantity = Number(document.getElementById('update-qty').value);
    const res = await fetch(`${API_URL}/products/${id}/quantity`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${token}`
      },
      body: JSON.stringify({ quantity })
    });
    if (res.ok) {
      show('products');
      fetchProducts();
      showMessage('Quantity updated!');
      updateForm.reset();
    } else {
      showMessage('Failed to update quantity.');
    }
  };

  // Initial state
  setNav(false);
  show('login');
}); 