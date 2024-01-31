
function getCsrfToken() {
    return document.querySelector('input[name="csrfmiddlewaretoken"]').value;
}


function makeLikeDislikeRequest(postId, action) {
    const csrfToken = getCsrfToken();
    const url = new URL('/blog/like_dislike/', window.location.origin);
    fetch(url, {
        method: 'POST',
        body: JSON.stringify({
            'postId': postId,
            'action': action
        }),
        headers: {
            'X-CSRFToken': csrfToken,
            'Content-Type': 'application/json'
        },
        credentials: 'include'
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

// Event listeners for the like and dislike buttons
document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.like-btn').forEach(button => {
        button.addEventListener('click', function() {
            const postId = this.dataset.postId;
            makeLikeDislikeRequest(postId, 'like');
        });
    });

    document.querySelectorAll('.dislike-btn').forEach(button => {
        button.addEventListener('click', function() {
            const postId = this.dataset.postId;
            makeLikeDislikeRequest(postId, 'dislike');
        });
    });
});

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