function validateForm() {
    var name = document.getElementById('name').value.trim();
    var email = document.getElementById('email').value.trim();
    var password = document.getElementById('password').value.trim();
    var number = document.getElementById('number').value.trim();
    var city = document.getElementById('city').value.trim();
    var errorMessage = '';
  
    // Basic validation for each field
    if (name === '') {
      errorMessage += 'Name is required.<br>';
    }
    if (email === '') {
      errorMessage += 'Email is required.<br>';
    } else if (!isValidEmail(email)) {
      errorMessage += 'Invalid email address.<br>';
    }
    if (password === '') {
      errorMessage += 'Password is required.<br>';
    }
    if (number === '') {
      errorMessage += 'Phone number is required.<br>';
    } else if (!isValidPhoneNumber(number)) {
      errorMessage += 'Invalid phone number format.<br>';
    }
    if (city === '') {
      errorMessage += 'City is required.<br>';
    }
  
    if (errorMessage !== '') {
      document.getElementById('message').innerHTML = '<div id="error">' + errorMessage + '</div>';
      return false;
    }
  
    return true;
  }
  
  function isValidEmail(email) {
    // Basic email validation using regex
    var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
  }
  
  function isValidPhoneNumber(number) {
    // Basic phone number validation (10 digits)
    var phoneRegex = /^\d{10}$/;
    return phoneRegex.test(number);
  }
  