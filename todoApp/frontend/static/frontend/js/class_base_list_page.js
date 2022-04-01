function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

var activeItem = null
var list_snapshot = []

buildList()

function buildList() {
    var wrapper = document.getElementById('list-wrapper')

    var url = 'http://127.0.0.1:8000/api/class_base/apiview/list_create/'

    fetch(url)
        .then((resp) => resp.json())
        .then(function (data) {

            var list = data
            for (var i in list) {

                try {
                    document.getElementById(`data-row-${i}`).remove()
                } catch (err) {

                }

                var title = `<span class="title">${list[i].title}<span>`
                if (list[i].completed == true) {
                    title = `<strike class="title">${list[i].title}</strike>`
                }

                var item = `
                <div id="data-row-${i}" class="task-wrapper flex-wrapper">
                    <div style="flex:7">
                        ${title}
                    </div>
                    <div style="flex:3">
                        <span class="category">${list[i].category}</span>
                    </div>
                    <div style="flex:1">
                        <button type="button" class="btn btn-sm btn-outline-info complete-info" data-toggle="modal" data-target="#exampleModal" data-whatever="@mdo">تکمیل</button>
                    </div>
                    <div style="flex:1">
                        <button class="btn btn-sm btn-outline-warning edit">ویرایش</button>
                    </div>
                    <div style="flex:1">
                        <button class="btn btn-sm btn-outline-dark delete">حذف</button>
                    </div>
                </div>
            `
                wrapper.innerHTML += item

            }

            if (list_snapshot.length > list.length) {
                for (var i = list.length; i < list_snapshot.length; i++) {
                    document.getElementById(`data-row-${i}`).remove()
                }
            }

            list_snapshot = list

            for (var i in list) {
                var editBtn = document.getElementsByClassName('edit')[i]
                var completeBtn = document.getElementsByClassName('complete-info')[i]
                var deleteBtn = document.getElementsByClassName('delete')[i]
                var title = document.getElementsByClassName('title')[i]

                editBtn.addEventListener('click', (function (item) {
                    return function () {
                        editItem(item)
                    }
                })(list[i]))

                completeBtn.addEventListener('click', (function (item) {
                    return function () {
                        completeInfo(item)
                    }
                })(list[i]))

                deleteBtn.addEventListener('click', (function (item) {
                    return function () {
                        deleteItem(item)
                    }
                })(list[i]))

                title.addEventListener('click', (function (item) {
                    return function () {
                        strikeUnstrike(item)
                    }
                })(list[i]))
            }

        })
}


var form = document.getElementById('form-wrapper')
form.addEventListener('submit', function (e) {
    e.preventDefault()
    var title = document.getElementById('title').value
    var url = 'http://127.0.0.1:8000/api/class_base/apiview/list_create/'
    if (activeItem != null) {
        var url = `http://127.0.0.1:8000/api/class_base/apiview/update_delete/${activeItem.id}/`
        fetch(url, {
            method: 'POST',
            headers: {
                'Content-type': 'application/json',
                'X-CSRFToken': csrftoken,
            },
            body: JSON.stringify({ 'title': title, 'completed': activeItem.completed })
        }).then(function (response) {
            buildList()
            document.getElementById('form').reset()
        })
        activeItem = null
    }
    else {

        fetch(url, {
            method: 'POST',
            headers: {
                'Content-type': 'application/json',
                'X-CSRFToken': csrftoken,
            },
            body: JSON.stringify({ 'title': title })
        }).then(function (response) {
            buildList()
            document.getElementById('form').reset()
        })

    }

})

function editItem(item) {
    activeItem = item
    document.getElementById('title').value = activeItem.title
}

function completeInfo(item) {
    document.getElementById('description').value = item.description
    document.getElementById('category').value = item.category
    if (item.priority == 'HIG') {
        p = 'بالا'
    }else if (item.priority == 'MED') {
        p = 'متوسط'
    }else {
        p = 'پایین'
    }
    console.log(document.getElementById('priority').value)
    document.getElementById('priority').value = document.getElementById(p).value
    var url = 'http://127.0.0.1:8000/api/class_base/apiview/category/list/'

    fetch(url)
    .then((resp) => resp.json())
    .then(function (data) {
        var list = data
        var modal_submit = document.getElementById('modal-submit')

        modal_submit.addEventListener("click", submitInfo);

        function submitInfo() {
            console.log('hellllllo')
            var description = document.getElementById('description').value
            var p = document.getElementById('priority').value

            if (p == 'بالا') {
                priority = 'HIG'
            } else if (p == 'متوسط') {
                priority = 'MED'
            } else {
                priority = 'LOW'
            }

            for (var i in list) {
                if (list[i].title == document.getElementById('category').value) {
                    var category = list[i]['title']
                }
            }
            var url = `http://127.0.0.1:8000/api/class_base/apiview/update_delete/${item.id}/`
            // console.log(item.title, item.completed, description, category, priority)
            console.log(item)
            fetch(url, {
                method: 'POST',
                headers: {
                    'Content-type': 'application/json',
                    'X-CSRFToken': csrftoken,
                },
                body: JSON.stringify({'title': item.title, 'completed': item.completed, 'description': description, 'category': category, 'priority': priority })
            }).then(function (response) {
                buildList()
                // document.getElementById('modal-form').reset()
            })
            // activeItem = null
        }

    })




}

function deleteItem(item) {
    var url = `http://127.0.0.1:8000/api/class_base/apiview/update_delete/${item.id}/`
    fetch(url, {
        method: 'DELETE',
        headers: {
            'Content-type': 'application/json',
            'X-CSRFToken': csrftoken,
        }
    }).then((response) => {
        buildList()
    })
}

function strikeUnstrike(item) {

    item.completed = !item.completed
    var url = `http://127.0.0.1:8000/api/class_base/apiview/update_delete/${item.id}/`
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({
            'title': item.title,
            'completed': item.completed
        })
    }).then((response) => {
        buildList()
    })
}

