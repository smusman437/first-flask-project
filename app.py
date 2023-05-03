from flask import Flask, request, jsonify

app = Flask(__name__)
POSTS = []

# GET all posts
@app.route('/posts', methods=["GET"])
def get_posts():
    return jsonify({'post': POSTS}), 201

# GET single post
@app.route('/posts/<int:post_id>')
def get_user(post_id):
    post = next((post for post in POSTS if post['id'] == post_id), None)
    if post:
        return jsonify(post)
    else:
        return jsonify({'message': 'Post not found'}), 404

# POST operation
@app.route('/posts', methods=['POST'])
def create_post():
    data = request.get_json()
    post = {'id':len(POSTS)+1,  'title': data['title'], 'content': data['content']}
    POSTS.append(post)
    return jsonify({'message': 'Post created successfully.'}), 201

# UPDATE operation
@app.route('/posts/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    post = next((post for post in POSTS if post['id'] == post_id), None)
    if post:
        data = request.get_json()
        post.update(data)
        return jsonify(post)
    else:
        return jsonify({'message': 'Post not found'}), 404
    
# DELETE operation
@app.route('/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    post = next((post for post in POSTS if post['id'] == post_id), None)
    if post:
        POSTS.remove(post)
        return jsonify({'message': 'Post deleted successfully.'}), 201   
    else:
        return jsonify({'message': 'Post not found'}), 404


app.run(debug=True, host="0.0.0.0", port=3002)