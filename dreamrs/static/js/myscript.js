var apercu = document.getElementById("apercu")

document.querySelector("#file").addEventListener("change", function(file){
    reader = new FileReader();
    reader.addEventListener("load", function(){
        apercu.src = this.result;
    })
    reader.readAsDataURL(this.files[0]);
})
