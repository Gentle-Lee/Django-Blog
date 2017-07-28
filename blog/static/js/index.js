
function ArrowBlink(arrow) {
	arrow.style.opacity = 1;
}
function Arrowout(arrow) {
	arrow.style.opacity = 0.5;
}

var clickCount = 0;
array = document.getElementsByClassName("navi");
function carousel (flag) {
	if (clickCount<0) {
		clickCount = 0;
		return 0;
	}
	clickCount = (clickCount + flag) %array.length;
	console.log(clickCount);
	array[clickCount].style.zIndex = "99";
	if(clickCount!=array.length-1){
		array[array.length-1].style.zIndex = "-111";
	}
	if(clickCount==0){
		array[clickCount+1].style.zIndex = "-111";
		clickCount = -1;
	}
	else if(clickCount == array.length-1){
		array[clickCount-1].style.zIndex = "-111";
	}
	else{
		array[clickCount-1].style.zIndex = "-111";
		array[clickCount+1].style.zIndex = "-111";
	}
}