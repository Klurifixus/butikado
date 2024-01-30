document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.like-btn').forEach(button => {
        button.addEventListener('click', function() {
            var postId = this.dataset.postId;
            makeLikeDislikeRequest(postId, 'like');
        });
    });

    document.querySelectorAll('.dislike-btn').forEach(button => {
        button.addEventListener('click', function() {
            var postId = this.dataset.postId;
            makeLikeDislikeRequest(postId, 'dislike');
        });
    });
});

function makeLikeDislikeRequest(postId, action) {
    const url = new URL('/blog/like_dislike/', window.location.origin);
    fetch(url, {
        method: 'POST',
        body: JSON.stringify({
            'postId': postId,
            'action': action
        }),
        headers: {
            'X-CSRFToken': getCookie('csrftoken'), // Function to get CSRF token from cookies
            'Content-Type': 'application/json'
        }
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        if (data.success) {
            document.getElementById('like-count-' + postId).innerText = data.likes;
            document.getElementById('dislike-count-' + postId).innerText = data.dislikes;
        }
    })
    .catch(error => {
        console.error('Error during fetch:', error);
    });
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}