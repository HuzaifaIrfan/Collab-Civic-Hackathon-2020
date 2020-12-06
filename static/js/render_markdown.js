


var render_markdown=(username,repo,branch,elementid)=>{

  fetch(`https://raw.githubusercontent.com/${username}/${repo}/${branch}/README.md`).then(response => response.text())
  .then(data => {
      //console.log(data)


      var markeddata= marked(data)

      var pattern=`<img src="https://raw.githubusercontent.com/${username}/${repo}/${branch}/`

      //var pattern=`<img src="https://github.com/${userprofileviewuser}/${userprofileviewuser}/raw/${default_branch}/`

      var replaceddata=markeddata.replaceAll('<img src="/', pattern)

      replaceddata=replaceddata.replaceAll('/blob/', '/raw/')


      var sourcesplitter = replaceddata.split('<img src="');

      // console.log(sourcesplitter)

      var rendered=sourcesplitter[0]

      for (var i=1; i<sourcesplitter.length;i++){


          var splel=sourcesplitter[i]

          var httpchar=splel.substring(0, 4)

          if(httpchar=="http"){

              rendered=rendered+'<img src="'

          }else{

              rendered=rendered+pattern

          }

          //console.log(httpchar)

          rendered=rendered+splel

      }


      

      document.getElementById(elementid).innerHTML =rendered
      });


    }

export {render_markdown}