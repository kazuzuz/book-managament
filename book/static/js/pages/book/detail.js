const showModalBtn = document.querySelector('#showModalBtn');
const modal = document.querySelector('#modal');
const closeModalBtn = document.querySelector('#closeModalBtn');
// document.querySelectorAll(".btn");

showModalBtn.addEventListener("click", function(e)
{
    modal.style.display = "block";
})

closeModalBtn.addEventListener("click", function()
{
    modal.style.display = "none";
})

function Check(){
    var checked = confirm("本当にお気に入り解除してよろしいですか？");
    if (checked == true) {
        return true;
    } else {
        return false;
    }
}

function getCookie(name){
    let cookieValue = null;
    if (document.cookie && document.cookie !== ''){
        console.log(document.cookie);
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++){
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')){
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1))
                break; 
            }}
    }
    return cookieValue;
}


// お気に入りの実装
function addFavorite(bookId){
    const csrftoken = getCookie('csrftoken');
    fetch(`/api/books/${bookId}/add_favorite`, {
        method: 'POST',
        headers:{
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        }
    }).then(response => {
        if (response.ok){
          addFavoriteBtn.classList.add('hidden');
          deleteFavoriteBtn.classList.remove('hidden');   
        }
        //async/await
        
    })
}

function deleteFavorite(bookId){
    const csrftoken = getCookie('csrftoken');
    fetch(`/api/books/${bookId}/delete_favorite`, {
        method: 'POST',
        headers:{
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        }
    }).then(response => {
        if (response.ok){
          addFavoriteBtn.classList.remove('hidden');
          deleteFavoriteBtn.classList.add('hidden');   
        }
        //async/await
        
    })
}

const addFavoriteBtn = document.querySelector('#favorite-add-btn');
const deleteFavoriteBtn = document.querySelector('#favorite-delete-btn');

addFavoriteBtn.addEventListener("click", function(e){
    const bookID = e.target.dataset.bookId;
    
    addFavorite(bookID);

});

deleteFavoriteBtn.addEventListener("click", function(e){
    const bookID = e.target.dataset.bookId;
    
    deleteFavorite(bookID);

});
