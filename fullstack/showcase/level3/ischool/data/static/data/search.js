
function search() {
    let url = document.querySelector('#search-url').value;
    let searchFor = document.getElementById('search-for').value;
    let extra = document.querySelector('#extra').value;
    let string = url + "?search=" + searchFor + extra;
    //console.log(string);
    //console.log(extra);
    fetch(string, {
        headers:{
          'Accept': 'application/json',
          'X-Requested-With': 'XMLHttpRequest',
        },
      })
      .then(res => { return res.json()})
      .then(data => {
        //console.log(data);
        let con = document.getElementById('elements');
        while(con.firstChild){
          con.removeChild(con.firstChild);
        }

        if(extra === "") {
        for (let i = 0; i < data.length; i++) {
        // append each person to our page
            const tr = document.createElement('tr');
            const td1 = document.createElement('td');
            const td2 = document.createElement('td');
            const td3 = document.createElement('td');
            const a = document.createElement('a');
            const button1 = document.createElement('button');
            const button2 = document.createElement('button');
            //div.innerText = {% if user.is_superuser %}
            a.className = "text-dark";
            a.href = `/course/${data[i].id}`;
            a.innerText = `${data[i].title}`;
            button1.className = "btn btn-success flex-right";
            button2.className = "btn btn-danger flex-right";
            button1.setAttribute('onclick', `return getUpdate(${data[i].id})`);
            button2.setAttribute('onclick', `return deleteItem(${data[i].id})`);
            button1.innerText = "Edit";
            button2.innerText = "Delete";
            td1.appendChild(a);
            td2.appendChild(button1);
            td3.appendChild(button2);
            tr.appendChild(td1);
            tr.appendChild(td2);
            tr.appendChild(td3);
            con.appendChild(tr);
        }
        }
        else if(extra.slice(1,7) == "course"){
        for (let i = 0; i < data.length; i++) {
            const tr = document.createElement('tr');
            const td1 = document.createElement('td');
            const td2 = document.createElement('td');
            const td3 = document.createElement('td');
            const td4 = document.createElement('td');
            const a = document.createElement('a');
            const button1 = document.createElement('button');
            const button2 = document.createElement('button');
            a.className = "text-dark";
            a.href = `/division/${data[i].id}`;
            a.innerText = `${data[i].title} `;
            td2.innerText = `${data[i].room}`;
            button1.className = "btn btn-success flex-right";
            button2.className = "btn btn-danger flex-right";
            button1.setAttribute('onclick', `return getUpdate(${data[i].id})`);
            button2.setAttribute('onclick', `return deleteItem(${data[i].id})`);
            button1.innerText = "Edit";
            button2.innerText = "Delete";
            td1.appendChild(a);
            td3.appendChild(button1);
            td4.appendChild(button2);
            tr.appendChild(td1);
            tr.appendChild(td2);
            tr.appendChild(td3);
            tr.appendChild(td4);
            con.appendChild(tr);
        }
        }
        else if(extra.slice(1,9) == "division"){
        for (let i = 0; i < data.length; i++) {
            const tr = document.createElement('tr');
            const td1 = document.createElement('td');
            const td2 = document.createElement('td');
            const td3 = document.createElement('td');
            const td4 = document.createElement('td');
            const td5 = document.createElement('td');
            const button1 = document.createElement('button');
            const button2 = document.createElement('button');
            td1.innerText = `${data[i].name} `;
            td2.innerText = `${data[i].surname} `;
            td3.innerText = `${data[i].grade}`;
            button1.className = "btn btn-success flex-right";
            button2.className = "btn btn-danger flex-right";
            button1.setAttribute('onclick', `return getUpdate(${data[i].id})`);
            button2.setAttribute('onclick', `return deleteItem(${data[i].id})`);
            button1.innerText = "Edit";
            button2.innerText = "Delete";
            td4.appendChild(button1);
            td5.appendChild(button2);
            tr.appendChild(td1);
            tr.appendChild(td2);
            tr.appendChild(td3);
            tr.appendChild(td4);
            tr.appendChild(td5);
            con.appendChild(tr);
        }
        }

      }).catch(error =>{
        console.log(error);
      });
    return false;

}


function search0() {
    let url = document.querySelector('#search0-url').value;
    let searchFor = document.getElementById('search0-for').value;
    let extra = document.querySelector('#extra0').value;
    let string = url + "?search=" + searchFor + extra;
    //console.log(string);
    //console.log(extra);
    fetch(string, {
        headers:{
          'Accept': 'application/json',
          'X-Requested-With': 'XMLHttpRequest',
        },
      })
      .then(res => { return res.json()})
      .then(data => {
        //console.log(data);
        let con = document.getElementById('elements0');
        while(con.firstChild){
          con.removeChild(con.firstChild);
        }
        for (let i = 0; i < data.length; i++) {
        // append each person to our page
            const div = document.createElement('div');
            const s = document.createElement('span');
            div.className = "bg-light flex";
            s.innerText = `${data[i].title}`;
            div.appendChild(s);
            con.appendChild(div);
        }
      }).catch(error =>{
        console.log(error);
      });
    return false;

}