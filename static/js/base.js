function searchPatient() {
    var input, filter, patients, name, i;
    input = document.getElementById("search");
    filter = input.value.toUpperCase();
    patients = document.getElementsByClassName("patient");
    for (i = 0; i < patients.length; i++) {
      name = patients[i].getElementsByTagName("td")[0].getElementsByTagName("a")[0];
      if (name.innerHTML.toUpperCase().indexOf(filter) > -1) {
        patients[i].style.display = "";
      } else {
        patients[i].style.display = "none";
      }
    }

}

function setActiveClass(){
    // var hasActiveClass = document.getElementsByClassName("active");
    // if(hasActiveClass){
    //     document.getElementsByClassName("active").classList=""
    // }
    // var url = location.pathname;
    // if(url="/"){
    //     console.log("hi");
    //     document.getElementById("home").classList="active"
    // }
        
    // else if(url="/patientslist/")   
    //     document.getElementById("patient").classList="active"
    
}
