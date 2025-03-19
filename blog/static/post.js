let getCsrfToken = () => {
    return document.cookie.split('csrftoken=')[1].split(';')[0]
}

let comment = (infoEl, postId) => {
    console.log(infoEl)
    let body = JSON.stringify(
        {
            author: infoEl.parentElement.querySelector("input").value,
            post: postId,
            info: infoEl.innerText,
        }
    )

    fetch("/comment/", {
        method: "post",
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCsrfToken()
        },
        body: body,
    }).then(() => location.reload())
}

const btns = document.getElementsByName("ans-btn")
const commentButton = document.getElementById("comment-btn")
const commentTextEl = document.getElementById("comment-text")
const postId = document.querySelector("meta[name='post-id']").content


const answer = (event) => {
    commentTextEl.innerText = event.target.parentElement.querySelector("strong").innerText + ", "
    commentTextEl.scrollIntoView()
}

commentButton.addEventListener("mouseup", () => {comment(commentTextEl, postId)})

for (let btn of btns){
    btn.addEventListener("mouseup", answer)
}
