function showMsg(msg) {
    document.getElementById("message").innerText = msg;
}

function register() {
    let name = document.getElementById("name").value.trim();
    let email = document.getElementById("email").value.trim();
    let password = document.getElementById("password").value.trim();

    if (!name || !email || !password) {
        return showMsg("Fill all fields");
    }

    if (localStorage.getItem(email)) {
        return showMsg("Account exists");
    }

    let user = { name, email, password };
    localStorage.setItem(email, JSON.stringify(user));

    showMsg("Register success");
}

function login() {
    let email = document.getElementById("email").value.trim();
    let password = document.getElementById("password").value.trim();

    let user = JSON.parse(localStorage.getItem(email));

    if (user && user.password === password) {
        localStorage.setItem("currentUser", email);
        window.location.href = "profile.html";
    } else {
        showMsg("Invalid login");
    }
}

function loadProfile() {
    let email = localStorage.getItem("currentUser");
    if (!email) return location.href = "login.html";

    let user = JSON.parse(localStorage.getItem(email));

    document.getElementById("name").value = user.name;
    document.getElementById("email").value = user.email;
}

function updateProfile() {
    let email = localStorage.getItem("currentUser");
    let user = JSON.parse(localStorage.getItem(email));

    user.name = document.getElementById("name").value;
    localStorage.setItem(email, JSON.stringify(user));

    showMsg("Updated");
}

function resetPassword() {
    let email = localStorage.getItem("currentUser");
    let user = JSON.parse(localStorage.getItem(email));

    let newPass = prompt("Enter new password:");
    if (!newPass) return;

    user.password = newPass;
    localStorage.setItem(email, JSON.stringify(user));

    showMsg("Password changed");
}

function deleteAccount() {
    let email = localStorage.getItem("currentUser");

    localStorage.removeItem(email);
    localStorage.removeItem("currentUser");

    alert("Account deleted");
    window.location.href = "login.html";
}
