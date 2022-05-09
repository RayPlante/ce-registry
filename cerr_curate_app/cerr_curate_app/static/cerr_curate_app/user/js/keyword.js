function addItem(){
  var ul = document.getElementById("dynamic-list");
  var candidate = document.getElementById("candidate");
  if (candidate.value !=='')
    var li = document.createElement("li");
    li.setAttribute('id','keyword');
    li.appendChild(document.createTextNode(candidate.value));
    li.innerHTML += "<button type=\"button\" onclick=\"removeItem()\">x"
    ul.appendChild(li);
}

function removeItem(){
    var id = event.target.closest("li");

	var ul = document.getElementById("dynamic-list");
  var candidate = document.getElementById("candidate");
  var item = document.getElementById(candidate.value);
  ul.removeChild(id);
}

var saveElement = function(event) {
    event.preventDefault();

    var list =  $("#dynamic-list").children()

        $.ajax({
            url: saveListUrl,
            data: { "list": list,
                  },
            dataType:"json",
            type: "post",
            success: function(data){
            },
            error: function(data){
                console.log(data)
            }
        })
}


