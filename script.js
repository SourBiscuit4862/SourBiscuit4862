// Function to handle comments and popups
function handleComments(comment) {
    const popups = {
        "123654": "This is an announcement popup!",
        "456321": "Upload video"
    };

    if (popups[comment]) {
        if (comment === "456321") {
            // Upload video popup
            const fileInput = document.createElement('input');
            fileInput.type = 'file';
            fileInput.accept = 'video/*';
            fileInput.addEventListener('change', handleFileUpload);
            fileInput.click();
        } else {
            // Other popups
            alert(popups[comment]);
        }
    } else {
        // Add comment to comment section
        addComment(comment);
    }
}

// Function to handle file upload
function handleFileUpload(event) {
    const file = event.target.files[0];
    if (file) {
        // You can implement logic to handle the uploaded file
        alert("File uploaded: " + file.name);
    }
}

// Example of listening to comments and triggering popups
document.getElementById("commentInput").addEventListener("keypress", function(event) {
    if (event.key === "Enter") {
        const comment = event.target.value.trim();
        if (comment) {
            handleComments(comment);
            event.target.value = "";
        }
    }
});
