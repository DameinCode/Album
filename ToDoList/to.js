document.addEventListener('click', (event) => {
  var status = event.target.dataset.btn
  if (status == "remoove") {
      event.target.parentNode.remove()
  } else if (status == "cool") {
      if (event.target.parentNode.getElementsByTagName('span')[0].style.textDecoration == 'line-through')
          event.target.parentNode.getElementsByTagName('span')[0].style.textDecoration = 'none'
      else
          event.target.parentNode.getElementsByTagName('span')[0].style.textDecoration = 'line-through'
  }
})

function addIT() {
    var what = document.getElementById('inp').value
    var toCheck = what.split(' ').join('');
    if(what === '' || toCheck === '') {
      alert("Write something")
      return 
    } 
    let newL = document.createElement('li')
    newL.className = 'newnew'
    newL.innerHTML = `<input type = "checkbox" data-btn = "cool">
                      <span>${what}</span>
                      <button class = "idk" data-btn = "remoove"><img src="https://cdn4.iconfinder.com/data/icons/social-messaging-ui-coloricon-1/21/52-512.png" /></button>
                      `
    document.getElementById('liist').appendChild(newL)
    document.getElementById('inp').value = ''
}