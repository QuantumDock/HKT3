function fileread(){
    fetch("static/html_dictionary.csv")
      .then(function(response) {
        if (response.ok) {
          return response.text();
        } else {
          throw new Error('File load error: ' + response.status);
        }
      })
      .then(function(fileContents) {
        let input = document.getElementById("dictionary__input").value;
        document.getElementById("placeholder").textContent = "";
        console.log(fileContents);
      })
      .catch(function(error) {
        console.error('File load error:', error);
      });
}