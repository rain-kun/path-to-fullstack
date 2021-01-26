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


function deleteItem(id) {
    let url = document.querySelector('#delete-url').value + id;
    let csrftoken = getCookie('csrftoken');
    //console.log(url);
    //console.log(extra);
    fetch(url, {
        method: 'DELETE',
        headers:{
          'Content-Type': 'application/json',
          'Accept': 'application/json',
          'X-Requested-With': 'XMLHttpRequest',
          'X-CSRFToken': csrftoken,
        },
      })
      .then(res => { return res.json()})
      .then(data => {
        alert("Deleted Successfully");
      })
      .then(location.reload())
      .catch(error =>{
        console.log(error);
      });
    return false;

}