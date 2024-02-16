document.addEventListener('DOMContentLoaded', function() {
    loadComments();

    document.getElementById('comment-form').addEventListener('submit', function(e) {
        e.preventDefault();
        const comment = document.getElementById('comment').value.trim();
        if (comment === '123654') {
            const announcement = document.createElement('h2');
            announcement.textContent = 'Announcement: ' + document.getElementById('announcement-text').value.trim();
            document.getElementById('announcement').appendChild(announcement);
        } else if (comment === '167543') {
            document.getElementById('video-upload-popup').style.display = 'block';
        }
        saveComment(comment);
        this.reset();
    });

    document.getElementById('upload-button').addEventListener('click', function() {
        // Handle video upload
        alert('Video uploaded successfully!');
        document.getElementById('video-upload-popup').style.display = 'none';
    });
});

function loadComments() {
    fetch('/get_comments')
        .then(response => response.json())
        .then(comments => {
            const commentsContainer = document.getElementById('comments');
            commentsContainer.innerHTML = '';
            comments.forEach(comment => {
                const commentElement = document.createElement('p');
                commentElement.textContent = comment;
                commentsContainer.appendChild(commentElement);
            });
        });
}

function saveComment(comment) {
    fetch('/save_comment', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ comment: comment }),
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
