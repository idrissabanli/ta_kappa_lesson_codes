blog_comments = [
    {
        'id': 1,
        'title': 'My Post',
        'comments': [
            {
                'id': 1,
                'content': 'Comment 1',
            },
            {
                'id': 2,
                'content': 'Comment 2',
            },
        ]
    },
    {
        'id': 2,
        'title': 'My Post 2',
        'comments': [
            {
                'id': 3,
                'content': 'Comment 3',
            },
        ]
    },
]

def create_blog(data):
    data.update({
        'comments': []
    })
    blog_comments.append(data)
    return blog_comments

def create_comment(data):
    # data = {
    #     'id': 2,
    #     'content': 'Comment 2',
    #     'blog_id': 1
    # }
    for blog in blog_comments:
        if blog['id'] == data['blog_id']:
            blog['comments'].append(data)
            break
     

def get_blog_comments():
    return blog_comments