/**
* Allow you to control modal state.
* If the modal is active, it will disabled, otherwise will be actived.
* @handler
* @param {string} modalId - The id of the modal container.
**/
function toggleModalState(modalId) {
    let modal = document.getElementById(modalId);
    
    if (modal.classList.contains("active")) {
        modal.classList.remove("active");
    } else {
        modal.classList.add("active")
    }
}

/**
* Allow you to hide the modal after clicking the background.
* @handler
* @param {object} event - The event that calls the function.
**/
function hideModalOnBgClick(event, modalId) {
    if (event.target.classList.contains("click-to-hide")) {
        toggleModalState(modalId);
    }
}