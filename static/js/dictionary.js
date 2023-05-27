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
        let dataArray = fileContents.split('\r\n').map(function(line) {
          return line.split(';'); // Split each line by comma
        });
        console.log(input)
        let phrase = "";
        let explanation = "";
        for(i = 0; i < dataArray.length; i++){
            if(input.toLowerCase().includes(dataArray[i][0].trim().toLowerCase())){
                phrase = dataArray[i][1];
                explanation = dataArray[i][2];
            }
            console.log(dataArray[i][0]);
        }
        document.getElementById("placeholder-title").textContent = phrase;
        document.getElementById("placeholder-text").textContent = explanation;
        if(phrase != ""){
            document.getElementById("placeholder-dash").textContent = " - ";
        }
      })
      .catch(function(error) {
        console.error('File load error:', error);
      });
}