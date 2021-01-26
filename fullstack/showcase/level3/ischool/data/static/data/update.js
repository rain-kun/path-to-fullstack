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

var pData;

function getUpdate(id) {
    let url = document.querySelector('#put-url').value + id;
    let pf = document.getElementById('put-form')
    let extra = document.getElementById('extra').value;
    let csrftoken = getCookie('csrftoken');
    //console.log(url);
    //console.log(extra);

    fetch(url, {
        headers:{
          'Content-Type': 'application/json',
          'Accept': 'application/json',
          'X-Requested-With': 'XMLHttpRequest',
        },
      })
      .then(res => { return res.json()})
      .then(data => {
        //console.log(data);
        while(pf.firstChild){
          pf.removeChild(pf.firstChild);
        }
        if(extra === "") {
        div = document.createElement('div');
        in1 = document.createElement('input');
        button = document.createElement('button');
        div.className = "mb-3";
        in1.value = data.title;
        in1.className = "put-title form-control";
        button.className = "btn btn-success";
        button.innerHTML = "Update";
        button.setAttribute('onclick', ` return updateItem(${data.id})`);
        div.appendChild(in1);
        pf.appendChild(div);
        pf.appendChild(button);
        }
        else if(extra.slice(1,7) == "course"){
        div = document.createElement('div');
        in1 = document.createElement('input');
        in2 = document.createElement('input');
        in3 = document.createElement('input');
        button = document.createElement('button');
        div.className = "mb-3";
        in1.value = data.title;
        in2.value = data.room;
        in3.value = data.course;
        in1.className = "put-title form-control";
        in2.className = "put-room form-control";
        in3.className = "put-course form-control";
        button.className = "btn btn-success";
        button.innerHTML = "Update";
        button.setAttribute('onclick', `return updateItem(${data.id})`);
        div.appendChild(in1);
        div.appendChild(in2);
        div.appendChild(in3);
        pf.appendChild(div);
        pf.appendChild(button);
        }
        else if(extra.slice(1,9) == "division"){
        div = document.createElement('div');
        in1 = document.createElement('input');
        in2 = document.createElement('input');
        in3 = document.createElement('input');
        in4 = document.createElement('input');
        button = document.createElement('button');
        div.className = "mb-3";
        in1.value = data.name;
        in2.value = data.surname;
        in3.value = data.grade;
        in4.value = data.division;
        in1.className = "put-name form-control";
        in2.className = "put-surname form-control";
        in3.className = "put-grade form-control";
        in4.className = "put-division form-control";
        button.className = "btn btn-success";
        button.innerHTML = "Update";
        button.setAttribute('onclick', `return updateItem(${data.id})`);
        div.appendChild(in1);
        div.appendChild(in2);
        div.appendChild(in3);
        div.appendChild(in4);
        pf.appendChild(div);
        pf.appendChild(button);
        }
      })
      .catch(error =>{
        console.log(error);
      });

    return false;

}

function updateItem(id) {
    let url = document.querySelector('#put-url').value + id;
    let pf = document.getElementById('put-form')
    let extra = document.getElementById('extra').value;
    let csrftoken = getCookie('csrftoken');
    let pData;
    console.log(url);
    if(extra === "") {
        pData = {
            title: document.querySelector('.put-title').value
        };
        }
        else if(extra.slice(1,7) == "course"){
        pData = {
            title: document.querySelector('.put-title').value,
            room: document.querySelector('.put-room').value,
            course: document.querySelector('.put-course').value
        };
        }
        else if(extra.slice(1,9) == "division"){
        pData = {
            name: document.querySelector('.put-name').value,
            surname: document.querySelector('.put-surname').value,
            grade: document.querySelector('.put-grade').value,
            division: document.querySelector('.put-division').value
        };
        }
    //console.log(extra);

    fetch(url, {
        method: 'PUT',
        headers:{
          'Content-Type': 'application/json',
          'Accept': 'application/json',
          'X-Requested-With': 'XMLHttpRequest',
          'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify(pData),
      })
      .then(res => { return res.json()})
      .then(data => {
        while(pf.firstChild){
          pf.removeChild(pf.firstChild);
        }
        alert("Updated Successfully");
      })
      .then(
      location.reload()
      )
      .catch(error =>{
        console.log(error);
      });
    return false;

}