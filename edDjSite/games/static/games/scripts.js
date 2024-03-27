const csrftoken = Cookies.get('csrftoken');
document.addEventListener('DOMContentLoaded', (event) => {
    const url_remove = document.querySelector('a.remove')
    const url_like = document.querySelector('a.like')


    const like_list = document.querySelectorAll('a.like')
    const remove_list = document.querySelectorAll('a.remove')

    const optionsPOST = () => {
        let options = {
            method: 'POST',
            headers: { 'X-CSRFToken': csrftoken },
            mode: 'same-origin'
        }
        return options
    }


    // Удаление комментария 
    remove_list.forEach(item => {
        item.addEventListener('click', function (e) {
            e.preventDefault()
            let id_el = item.dataset.id

            options = optionsPOST()

            let formDataComment = new FormData();
            formDataComment.append('id', id_el);
            options['body'] = formDataComment;

            fetch(url_remove.dataset.url, options).then(res => (res.json()))
                .then(data => {
                    if (data['status'] === 'ok') {
                        document.querySelector(`div.comment-body[data-id="${id_el}"]`).remove()

                        let commentCount = document.querySelector('span.count_comment')
                        let totalComment = parseInt(commentCount.innerHTML)
                        commentCount.innerHTML = totalComment - 1
                    }
                })
        })
    })

    // Добавление или удаление лайка под записью
    like_list.forEach(item => {
        item.addEventListener('click', function (e) {
            e.preventDefault()
            let likeButton = this;

            let options = optionsPOST()

            let formData = new FormData();
            formData.append('id', likeButton.dataset.id);
            formData.append('action', likeButton.dataset.action);
            options['body'] = formData;

            fetch(url_like.dataset.url, options).then(response => (response.json()))
                .then(data => {
                    if (data['status'] === 'ok') {
                        let prevAction = likeButton.dataset.action;

                        let action = prevAction === 'like' ? 'unlike' : 'like';
                        let id_el = item['dataset'].id;
                        let el = document.querySelector(`a.like[data-id="${id_el}"] .heart`)
                        let style = el.getAttribute('name')

                        el.setAttribute('name', style === 'heart' ? 'heart-outline' : 'heart')
                        likeButton.dataset.action = action;

                        let likeCount = el.parentNode.nextElementSibling
                        let totalLike = parseInt(likeCount.innerHTML)
                        likeCount.innerHTML = prevAction === 'like' ? totalLike + 1 : totalLike - 1;

                    }
                })

        })
    })

})