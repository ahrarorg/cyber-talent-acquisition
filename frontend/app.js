const API_URL = 'http://localhost:8000';

async function fetchWorkRoles() {
    try {
        const response = await fetch(`${API_URL}/work-roles`);
        const roles = await response.json();
        const list = document.getElementById('work-roles-list');
        const select = document.getElementById('work-role-select');
        
        list.innerHTML = '';
        roles.forEach(role => {
            const div = document.createElement('div');
            div.className = 'card';
            div.innerHTML = `
                <div class="role-id">[ ${role.id} ]</div>
                <h3>${role.name}</h3>
                <p>${role.description}</p>
            `;
            list.appendChild(div);

            const option = document.createElement('option');
            option.value = role.id;
            option.textContent = role.name;
            select.appendChild(option);
        });
    } catch (e) { console.error("Failed to fetch roles", e); }
}

async function fetchOperatives() {
    try {
        const response = await fetch(`${API_URL}/operatives`);
        const operatives = await response.json();
        const list = document.getElementById('operatives-list');
        
        list.innerHTML = '';
        if (operatives.length === 0) {
            list.innerHTML = '<p style="color:#555">No operatives identified in sector.</p>';
            return;
        }

        operatives.forEach(op => {
            const div = document.createElement('div');
            div.className = 'card';
            div.innerHTML = `
                <h3>ALIAS: ${op.alias}</h3>
                <p>COMMS: ${op.email}</p>
            `;
            list.appendChild(div);
        });
    } catch (e) { console.error("Failed to fetch operatives", e); }
}

document.getElementById('mission-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const codename = document.getElementById('mission-codename').value;
    const roleId = document.getElementById('work-role-select').value;

    try {
        const response = await fetch(`${API_URL}/missions`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                codename: codename,
                work_role_id: roleId,
                objective: `Classified mission for ${roleId}`
            })
        });

        if (response.ok) {
            alert('MISSION DEPLOYED TO NETWORK.');
            document.getElementById('mission-form').reset();
        }
    } catch (e) { alert('DEPLOYMENT FAILED.'); }
});

document.addEventListener('DOMContentLoaded', () => {
    fetchWorkRoles();
    fetchOperatives();
});
