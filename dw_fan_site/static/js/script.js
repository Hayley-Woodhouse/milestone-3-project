document.addEventListener('DOMContentLoaded', function() {
  // https://materializecss.com/navbar.html#! mobile menu
    let sidenav = document.querySelectorAll('.sidenav');
    M.Sidenav.init(sidenav);
  });

  // toggle to view hiden password https://www.w3schools.com/howto/howto_js_toggle_password.asp
  function showPasswords() {
    let x = document.getElementById("password_user");
    let y = document.getElementById("password2");
    if (x.type === "password") {
      x.type = "text";
    } else {
      x.type = "password";
    }
    if (y.type === "password") {
      y.type = "text";
    } else {
      y.type = "password";
    }
  }
    