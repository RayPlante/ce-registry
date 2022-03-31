function addItem(){
  var ul = document.getElementById("dynamic-list");
  var candidate = document.getElementById("candidate");
  if (candidate.value !=='')
    var li = document.createElement("li");
    li.setAttribute('id','keyword');
    li.appendChild(document.createTextNode(candidate.value));
    ul.appendChild(li);
}

function removeItem(){
	var ul = document.getElementById("dynamic-list");
  var candidate = document.getElementById("candidate");
  var item = document.getElementById(candidate.value);
  ul.removeChild(item);
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


