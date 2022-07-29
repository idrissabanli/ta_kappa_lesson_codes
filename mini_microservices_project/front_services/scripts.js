const createPostForm = document.getElementById('create-post');
const postListSection = document.querySelector('#post-list');

document.addEventListener("DOMContentLoaded",async function(event) {
    await getPosts();
});

async function getPosts(){
    let res = await fetch('http://127.0.0.1:5002/api/posts');
    let posts = await res.json();
    for (const post of posts) {
        await renderPost(post);
    }
}


async function renderPost(post){
    let postComments = post.comments || [] // await getComments(post_id=post.id);
    // let listComments = '';
    // for (const comment of postComments) {
    //     listComments += `<li>${comment.content}</li>`
    // }
    postListSection.innerHTML += `
    <div class="col-4">
                <div class="card p-4">
                    <h4>${post.title}</h4>
                    <ul>
                        ${ postComments.map(comment => `<li>${comment.content}</li>`).join('')}
                    </ul>
                    <form post-id=${post.id} class="create-comment">
                        <div class="form-group">
                            <label for="">Comment</label>
                            <input type="text" name="content" class="form-control">
                        </div>
                       <input class="btn btn-primary" type="submit" value="Save">
                    </form>
                </div>
                
            </div>
    `
    // prompt('Daxil edin!')
    // assignEvent();
    
    // console.log(document.querySelectorAll('.create-comment'));
}

async function getComments(post_id){
    let res = await fetch(`http://127.0.0.1:5001/posts/${post_id}/comments`);
    let comments = await res.json();
    return comments;
}


createPostForm.addEventListener('submit', async (event)=>{
    event.preventDefault();
    let postData = {
        'title': createPostForm.title.value
    }
    const res = await fetch('http://127.0.0.1:5000/api/posts', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(postData)
    });
    const post = await res.json();
    renderPost(post);
});

document.addEventListener('submit', async function(event){
    event.preventDefault();
    let commentForm = event.target;
    if(commentForm.classList.contains('create-comment')){
        let postId = commentForm.getAttribute('post-id');
        let postData = {
            'content': commentForm.content.value
        }
        const res = await fetch(`http://127.0.0.1:5001/posts/${postId}/comments`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(postData)
        }).catch((error) => {
            // Your error is here!
            alert('Something went wrong!');
          });;
        if (res.ok){
            const comment = await res.json();
            commentForm.previousSibling.previousSibling.innerHTML += `<li>${comment.content}</li>`;
        }else{
            alert('Something went wrong!');
        }
        
        // renderPost(post);
    }
    // alert(event.target.classList);
});

// function assignEvent(){
//     let commentForms = document.querySelectorAll('.create-comment');
//     // console.log('commentForms', commentForms);
    
//     commentForms.forEach((commentForm) =>{
//         commentForm.addEventListener('submit', function(event){
//             event.preventDefault();
//             alert('Worked');
//         })
//     })
//     console.log('Assigned to ', commentForms.length, ' form')
// }


