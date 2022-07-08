window.addEventListener('load', async function() {
    let response = await fetch('http://localhost:8000/api/categories/');
    let categories = await response.json();
    for(let category of categories){
        document.querySelector('[name="category"]').innerHTML += `
        <option value="${category.id}">${category.title}</option>
        `
    }
})

let form = document.querySelector('#blog-form');

form.addEventListener('submit', async function(event){
    event.preventDefault();
    console.log('here');
    
    let postData = new FormData(form);
    let response = await fetch('http://localhost:8000/api/recipes/', {
        headers: {
            'Authorization': "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjU3Mjk5NDY3LCJpYXQiOjE2NTcyOTkxNjcsImp0aSI6ImU0ZWQ5MzZmNDM1NjQ1OTU5ZGU4MGY0ZTMzNzBiNDk0IiwidXNlcl9pZCI6Mn0.BuAb6MnddH4KSKv_8-igU3rkQOaTn0lIzKgUOzJVpS0"
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