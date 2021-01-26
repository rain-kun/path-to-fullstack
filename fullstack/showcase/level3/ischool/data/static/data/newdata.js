function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


function addCourse() {

    let url = document.querySelector('#post-url').value;
    let csrftoken = getCookie('csrftoken');
    let data ={
        title: document.getElementById('course').value
    };
    fetch(url, {
        method: 'POST',
        credentials: 'same-origin',
        headers:{
          'Content-Type': 'application/json',
          'Accept': 'application/json',
          'X-Requested-With': 'XMLHttpRequest',
          'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify(data),
      })
      .then(res => { return res.json()})
      .then(data => {
        alert("Course Created Successfully");
      })
      .then(location.reload())
      .catch(error =>{
        console.log(error);
      });
    return false;
}

function addDivision() {
    let url = document.querySelector('#post-url').value;
    let csrftoken = getCookie('csrftoken');
    let data ={
        title: document.getElementById('division').value,
        room: document.getElementById('roomno').value,
        course: document.getElementById('course').value
    };
    fetch(url, {
        method: 'POST',
        credentials: 'same-origin',
        headers:{
          'Content-Type': 'application/json',
          'Accept': 'application/json',
          'X-Requested-With': 'XMLHttpRequest',
          'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify(data),
      })
      .then(res => { return res.json()})
      .then(data => {
        alert("Division Created Successfully");
      })
      .then(location.reload())
      .catch(error =>{
        console.log(error);
      });
    return false;
}

function addStudent() {
    let url = document.querySelector('#post-url').value;
    let csrftoken = getCookie('csrftoken');
    let data ={
        name: document.getElementById('name').value,
        surname: document.getElementById('surname').value,
        grade: document.getElementById('grade').value,
        division: document.getElementById('division').value
    };
    fetch(url, {
        method: 'POST',
        credentials: 'same-origin',
        headers:{
          'Content-Type': 'application/json',
          'Accept': 'application/json',
          'X-Requested-With': 'XMLHttpRequest',
          'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify(data),
      })
      .then(res => { return res.json()})
      .then(data => {
        alert("Student Created Successfully");
      })
      .then(location.reload())
      .catch(error =>{
        console.log(error);
      });
    return false;
}