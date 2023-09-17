  var data = document.body.parentElement.outerHTML
  var links = []
  var dir = /biblioteka/r/lekcije/
  var key = 'a href="' + dir
  for(var i = 0; i < data.length; i++) {
      var p = data[i], id = "", link = ""
      for(var e = 0; e < key.length; e++) {
          id += data[i+e]
          }
      if(id != key) { continue }
      
      for(var e = key.length; e < data.length; e++) {
          if(data[e+i] == '"') { break }
          link += data[i+e]
          }
        links.push(dir + link)
      };

  url = document.URL.replace("https://petlja.org", "")
  document.write(url + "<br>")

  for(var i = 0; i < links.length; i++) { 
       document.write(links[i] + "<br>")
   }