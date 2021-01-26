
function load_mailbox(mailbox) {

  // Show the mailbox and hide other views
  document.querySelector('#compose-view').style.display = 'none';
  document.querySelector('#emails-detail').style.display = 'none';
  document.querySelector('#emails-view').style.display = 'block';

  // Show the mailbox name
  document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;


  document.querySelector('.container-sm').innerHTML = ''

  //get the data
  fetch(`/emails/${mailbox}`)
    .then(response => response.json())
    .then(emails => {
      // Print emails
      // create the html element
      for (let i = 0, n = emails.length; i < n; i++) {
        let email = emails[i]
        const div = document.createElement('div')
        div.classList.add("row", 'border', 'border-primary')
        if (!email.read) {
          div.classList.add("bg-light")
        }
        const left = document.createElement('div')
        left.classList.add("col-sm")
        const right = document.createElement('div')
        right.classList.add("col-sm")
        left.innerHTML = (`From: ${email.sender} Subject: ${email.subject}`)
        right.innerHTML = (`TimeStamp: ${email.timestamp}`)
        div.appendChild(left)
        div.appendChild(right)
        div.addEventListener('click', () => load_mail(email.id, mailbox))
        document.querySelector('#emails-view').appendChild(div)

      }

      // ... do something else with emails ...
    }).catch(error =>{
      console.log(error)
    });



}

function load_mail(id, box) {

  document.querySelector('#emails-detail').value = ''


  document.querySelector('#emails-view').style.display = 'none'
  document.querySelector('#compose-view').style.display = 'none'
  document.querySelector('#emails-detail').style.display = 'block'
  if (box === 'inbox') {
    fetch(`/emails/${id}`, {
      method: 'PUT',
      body: JSON.stringify({
        read: true,
      })
    })
  }
  fetch(`/emails/${id}`)
    .then(response => response.json())
    .then(email => {
      // Print email
      console.log(email)

      // ... do something else with email ...

      const div = document.createElement('div')
      div.classList.add('row', 'border', 'border-primary', 'rounded-bottom')
      const left = document.createElement('div')
      left.classList.add("col-sm")
      const right = document.createElement('div')
      right.classList.add("col-sm")
      right.innerHTML = (`TimeStamp:${email.timestamp}`)
      left.innerHTML = (`From: ${email.sender}`)
      const center = document.createElement('div')
      center.classList.add("container")
      center.innerHTML = (`<strong>Subject: ${email.subject}</strong>
        <div><strong>recipients: </strong>${email.recipients}</div>
              <strong>Body:</strong><p class="para">${email.body}</p>`)
      const but = document.createElement('button')
      const rep = document.createElement('button')
      if (box === "archive") {
        but.innerHTML = "Remove"
      } else if(box==='inbox') {
        but.innerHTML = "Archive"
      }
      if(box != "sent"){
        but.classList.add('btn', 'btn-outline-primary')
        rep.classList.add('btn', 'btn-outline-primary')
        rep.innerHTML = "Reply"
        center.appendChild(but)
        center.appendChild(rep)
      }
      div.appendChild(left)
      div.appendChild(right)
      div.appendChild(center)
      document.querySelector('#detail-container').appendChild(div)

      but.addEventListener('click', () => {

        if (box === 'archive') {
          console.log("yes")
          fetch(`/emails/${id}`, {
            method: 'PUT',
            body: JSON.stringify({
              archived: false
            })
          })
          load_mailbox('inbox')
        } else if(box==='inbox'){
          fetch(`/emails/${id}`, {
            method: 'PUT',
            body: JSON.stringify({
              archived: true
            })
          })
          load_mailbox('inbox')
        }
      })

      rep.addEventListener('click', () => compose_reply(email.id))
    })
}
