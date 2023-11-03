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