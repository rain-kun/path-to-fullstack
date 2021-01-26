
function compose_email() {

  // Show compose view and hide other views
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#emails-detail').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'block';


  // Clear out composition fields
  document.querySelector('.head').innerHTML = 'New Mail';
  document.querySelector('#compose-recipients').value = '';
  document.querySelector('#compose-recipients').disabled = false;
  document.querySelector('#compose-subject').value = '';
  document.querySelector('#compose-body').value = '';
  document.querySelector('.container-sm').innerHTML = '';

  // submit function
  document.querySelector('#compose-form').onsubmit = () => {


    fetch('/emails', {
        method: 'POST',
        body: JSON.stringify({
          recipients: document.querySelector('#compose-recipients').value,
          subject: document.querySelector('#compose-subject').value,
          body: document.querySelector('#compose-body').value,
          read: false,
          archived: false,
        })
      })
      .then(response => response.json())
      .then(result => {
        // Print result
        console.log(result);
      }).catch(error =>{
        console.log(error);
      });


    //load sent mailbox
    document.querySelector('#compose-view').style.display = 'none';
    document.querySelector('#emails-view').style.display = 'block';
    return false;
  }
}


function compose_reply(id){
  // Show compose view and hide other views
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#emails-detail').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'block';

  //get the data
  fetch(`/emails/${id}`)
    .then(response => response.json())
    .then(email => {
      // Print email
      // console.log(email);
      let temp = email.subject;
      document.querySelector('#compose-recipients').value = `${email.sender}`;
      document.querySelector('#compose-subject').value = "Re:"+temp.replace(/Re:/," ");
      document.querySelector('#compose-body').value = `On ${email.timestamp} ${email.sender} wrote: \n ${email.body} \n Reply:`;
    });

  // prefill composition fields
  document.querySelector('#compose-recipients').disabled = true;
  document.querySelector('.head').innerHTML = 'Reply';
  document.querySelector('.container-sm').innerHTML = '';

  // submit function
  document.querySelector('#compose-form').onsubmit = () => {


    fetch('/emails', {
        method: 'POST',
        body: JSON.stringify({
          recipients: document.querySelector('#compose-recipients').value,
          subject: document.querySelector('#compose-subject').value,
          body: document.querySelector('#compose-body').value,
        })
      })
      .then(response => response.json())
      .then(result => {
        // Print result
        console.log(result);
      });


    //load sent mailbox
    document.querySelector('#compose-view').style.display = 'none';
    document.querySelector('#emails-view').style.display = 'block';
    return false;
  }
}
