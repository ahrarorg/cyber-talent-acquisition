const API_URL = 'http://localhost:8000';
async function fetchWorkRoles() {
    const response = await fetch(`${API_URL}/work-roles`);
    const roles = await response.json();
    const list = document.getElementById('work-roles-list');
    const select = document.getElementById('work-role-select');
    list.innerHTML = '';
    roles.forEach(role => {
        const div = document.createElement('div');
        div.className = 'card card-body';
        div.innerHTML = `
            <h5>${role.name} (${role.id})</h5>
            <p>${role.description}</p>
            <small>Tasks: ${role.tasks.join(', ')}</small>
        `;
        list.appendChild(div);
        const option = document.createElement('option');
        option.value = role.id;
        option.textContent = role.name;
        select.appendChild(option);
    });
}
async function fetchCandidates() {
    const response = await fetch(`${API_URL}/candidates`);
    const candidates = await response.json();
    const list = document.getElementById('candidates-list');
    list.innerHTML = '';
    if (candidates.length === 0) {
        list.innerHTML = '<p class="text-muted">No candidates registered yet.</p>';
        return;
    }
    candidates.forEach(candidate => {
        const div = document.createElement('div');
        div.className = 'card card-body';
        div.innerHTML = `
            <h5>${candidate.name}</h5>
            <p>Email: ${candidate.email}</p>
            <p>Applied for: ${candidate.applied_role_id}</p>
        `;
        list.appendChild(div);
    });
}
document.getElementById('job-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const title = document.getElementById('job-title').value;
    const roleId = document.getElementById('work-role-select').value;
    const response = await fetch(`${API_URL}/job-postings`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            title: title,
            work_role_id: roleId,
            description: `New job for ${roleId}`
        })
    });
    if (response.ok) {
        alert('Job posting created successfully!');
        document.getElementById('job-form').reset();
    }
});
document.addEventListener('DOMContentLoaded', () => {
    fetchWorkRoles();
    fetchCandidates();
});
