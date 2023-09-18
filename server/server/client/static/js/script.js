$('.search-button').click(function () {
	$(this).parent().toggleClass('open');
});
var prev = document.getElementById('prev');
var next = document.getElementById('next');
var trak = document.getElementById('progress');
var step = document.getElementById('step');

next.addEventListener('click', function () {
	var cls = trak.className.split('-').pop();
	cls > 3 ? cls = 1 : cls++;
	checkstep(cls);

	step.innerHTML = cls;
	trak.className = 'progress-' + cls;
});

prev.addEventListener('click', function () {
	var cls = trak.className.split('-').pop();
	cls < 2 ? cls = 3 : cls--;
	checkstep(cls);
	step.innerHTML = cls;
	trak.className = 'progress-' + cls;
});


function checkstep(cls) {
	var container = document.getElementById('controls');
	var divIndex = cls - 1;
  
	for (let index = 0; index < container.children.length; index++) {
	  if (index === divIndex) {
		container.children[divIndex].classList.add('show');
	  } else {
		container.children[index].classList.remove('show');
	  }
	}
  }
  