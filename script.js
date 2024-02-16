// Function to show popup
function showPopup(popupId) {
    const popup = document.getElementById(popupId);
    popup.style.display = "block";
}

// Function to handle comments
function handleCommentSubmit(event) {
    event.preventDefault();
    const commentInput = document.getElementById("commentInput");
    const comment = commentInput.value.trim();
    if (comment !== "") {
        addComment(comment);
        commentInput.value = "";
    }
}

// Function to add comment to the comment section
function addComment(comment) {
    const commentsDiv = document.getElementById("comments");
    const commentDiv = document.createElement("div");
    commentDiv.textContent = comment;
    commentsDiv.appendChild(commentDiv);
}
