const createPostForm = document.getElementById('create-post');
const postListSection = document.querySelector('#post-list');

document.addEventListener("DOMContentLoaded",async function(event) {
    await getPosts();
});

async function getPosts(){
    let res = await fetch('http://127.0.0.1:5000/api/posts');
    let posts = await res.json();
    for (const post of posts) {
        await renderPost(post);
    }
}


async function renderPost(post){
    let postComments = await getComments(post_id=post.id);
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
                    <form class="create-comment">
                        <div class="form-group">
                            <label for="">Comment</label>
                            <input type="text" class="form-control">
                        </div>
                       <input class="btn btn-primary" type="submit" value="Save">
                    </form>
                </div>
                
            </div>
    `
    console.log(document.querySelectorAll('.create-comment'));
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

