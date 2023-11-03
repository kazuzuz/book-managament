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
