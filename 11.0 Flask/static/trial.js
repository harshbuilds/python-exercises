let signedIn = false;
let message = document.getElementById("message");
let googleAuth = document.getElementsByClassName("googleLogin")[0];
let logout = document.getElementsByClassName("logout")[0];
let logoutBtn = document.getElementById("logoutBtn")
let testreq = document.getElementById("testreq")

async function handleGoogleLogin(response) {
  console.log(response);
  await fetch('http://localhost:8096/verifyGoogleToken', {
    method: 'POST',
    headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json',
      'Authorization': getToken(),
    },
    body: JSON.stringify(response)
  }).then((res) => {
    if (res.ok) {
      return res.json();
    }
    return {error: "An error occured"}
  }).then((res) => {
    if (res.valid == true) {
      console.log(res);
      setToken(res['token']);
      loggedIn()
    } else {
      console.log("Invalid token");
      console.log(res);
    }
  });
}

function loggedIn() {
  signedIn = true;
  message.innerText = "Logged in";
  googleAuth.classList.toggle("collapse");
  logout.classList.toggle("collapse");
}

function logoutUser() {
  clearToken()
  signedIn = false;
  message.innerText = "Not Logged in";
  googleAuth.classList.toggle("collapse");
  logout.classList.toggle("collapse");
}

function clearToken() {
  sessionStorage.removeItem('token');
}

function getToken() {
  return sessionStorage.getItem("token");
}

function setToken(token) {
  sessionStorage.setItem("token", token);
}

logoutBtn.addEventListener("click", (event) => {
  logoutUser();
});

testreq.addEventListener("click", async (event) => {
  await fetch('http://localhost:8096/user_data', {
    method: 'GET',
    headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json',
      'Authorization': getToken(),
    },
  }).then((res) => {
    if (res.ok) {
      return res.json();
    }
    return {error: "An error occured"}
  }).then((res) => {
    if (res.success == true) {
      console.log("Data retrieval successful")
      console.log(res);
    } else {
      console.log("Invalid or no token");
      console.log(res);
    }
  });
})

function checkToken() {
    if (getToken()) {
        loggedIn()
    }
}
checkToken()

// {
  //   clientId: "204262850104-0ali0oakr8rs8e0d0b8097rk61l65ei8.apps.googleusercontent.com"
  //   client_id: "204262850104-0ali0oakr8rs8e0d0b8097rk61l65ei8.apps.googleusercontent.com"
  //   credential: "eyJhbGciOiJSUzI1NiIsImtpZCI6IjZmOTc3N2E2ODU5MDc3OThlZjc5NDA2MmMwMGI2NWQ2NmMyNDBiMWIiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL2FjY291bnRzLmdvb2dsZS5jb20iLCJhenAiOiIyMDQyNjI4NTAxMDQtMGFsaTBvYWtyOHJzOGUwZDBiODA5N3JrNjFsNjVlaTguYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCJhdWQiOiIyMDQyNjI4NTAxMDQtMGFsaTBvYWtyOHJzOGUwZDBiODA5N3JrNjFsNjVlaTguYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCJzdWIiOiIxMTQ4ODI1MDkzNzE0Njc0MTEwNTYiLCJlbWFpbCI6ImhhcnNodmVlcnNhQGdtYWlsLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJuYmYiOjE3MDkyMDQyMjUsIm5hbWUiOiJIYXJzaCBWZWVyc2EiLCJwaWN0dXJlIjoiaHR0cHM6Ly9saDMuZ29vZ2xldXNlcmNvbnRlbnQuY29tL2EvQUNnOG9jSVRHUFJabWVrRzVIOUlMUFRhbml0ZzlQQXJZM3BNSEFMMUFuM29seC1EPXM5Ni1jIiwiZ2l2ZW5fbmFtZSI6IkhhcnNoIiwiZmFtaWx5X25hbWUiOiJWZWVyc2EiLCJsb2NhbGUiOiJlbiIsImlhdCI6MTcwOTIwNDUyNSwiZXhwIjoxNzA5MjA4MTI1LCJqdGkiOiJjNmI5ZDk5ZmRmMzlkMTMxOTcyOTgzZjk0N2FmMTg4NWFiMmRmMDJhIn0.PvXclmT2JPwl2qIVQpemknPuvfyvEoDTTOz92_Y4tEJ43a2uhlkrAAek4zS3WEaXM_yEM5qNVkyody_7EngByRzhSAwq7EU_YzkLuaCZHjCuqDg-wwG_iPvDqTSLRAmCBkz2x6TUm-TdCCZamkMmDasgQFi016LMztfQSjblZP74omo0BdnTHCE1WEmZ4hkOyiXkrXWvNzq0vCbsXDQYS1MYmNODCl9Adbr2rTE5piuy3hDq0MXol2UcdpkIGYNXlaWYxipwYEr6ezd_ny6a6eFRbE5DjY5-6xQLAQ4xoyX6kYEU5YAvTrnR2jRMun8NwzopbPImBd1urJqfELZB4A"
  //   select_by: "btn"