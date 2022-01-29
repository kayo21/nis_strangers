
function get_data() {
    response = fetch("http://cerebrium.kz/api/data_finance/?name=arsen&id=5");
    response.json().then(data => {
        alert(data.fm)
    })
}

function register_user(){
	input_mail = document.getElementById("email")
	mail = input_mail.value
	input_password = document.getElementById("password")
	password = input_password.value
	"wedwedwedwed" + "333"
    response = fetch("/api/register_user?mail="+mail+"&password="+password);
    response.json().then(data => {
    })
}

const switchers = [...document.querySelectorAll('.switcher')]

switchers.forEach(item => {
	item.addEventListener('click', function() {
		switchers.forEach(item => item.parentElement.classList.remove('is-active'))
		this.parentElement.classList.add('is-active')
	})
})

