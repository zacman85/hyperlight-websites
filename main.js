function changeSplashPage(button) {
	var href = button.href;
	var pos = href.indexOf("#");
	if (pos < 0 || pos == (href.length + 1)) return false;
	var target = document.getElementById(href.substring(pos + 1));
	if (target === null) return false;
	var current = document.querySelectorAll("#splash-content article.show");
	for (var i = 0; i < current.length; i++) current[i].className = null;
	target.className = "show";
	return false;
}

function changeBodyStyleModel(select) {
	console.log(select.value);
	return false;
}

function handleSearchForm(form) {
	var searchQuery = document.getElementById("search-box").value;
	document.location.href = "https://www.caranddriver.com/search/" + window.encodeURIComponent(searchQuery);
	return false;
}

window.onLoad = function() {

}
