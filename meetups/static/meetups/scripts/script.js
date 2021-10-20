function showModal() {
	let modal = document.getElementById("modal-background");
	let span = document.getElementsByClassName("close")[0];
	modal.style.display = 'block';
	span.onclick = () => modal.style.display = 'none';
	window.onclick = event => {
		if(event.target === modal){
			modal.style.display = 'none';
		}
	}

	
}