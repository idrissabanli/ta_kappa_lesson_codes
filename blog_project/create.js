window.addEventListener('load', async function() {
    let userDetail = JSON.parse(localStorage.getItem('user-detail'));
    if (!userDetail || !userDetail.access){
        window.location = '/login.html';
    }
    let response = await fetch('http://localhost:8000/api/categories/');
    let categories = await response.json();
    for(let category of categories){
        document.querySelector('[name="category"]').innerHTML += `
        <option value="${category.id}">${category.title}</option>
        `
    }
});

let form = document.querySelector('#blog-form');

form.addEventListener('submit', async function(event){
    event.preventDefault();
    console.log('here');
    let userDetail = JSON.parse(localStorage.getItem('user-detail'));
    if (!userDetail || !userDetail.access){
        window.location = '/login.html';
    }
    let postData = new FormData(form);
    
    let response = await fetch('http://localhost:8000/api/recipes/', {
        headers: {
            'Authorization': `Bearer ${userDetail.access}`
        },
        method: 'POST',
        body: postData,
    });
    if(response.ok){
        window.location = '/'
    }else{
        alert('Something went wrong!');
    }
})