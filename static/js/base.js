

function datePicker(){
    var days, i;
    days = document.getElementsByClassName("jdp-day");
    for(i =0; i < days.length; i++){
      days[i].addEventListener("click",function(){
          document.querySelector("#publishDateMax").value = document.querySelector("#publishDateMax").value.replaceAll("/","-");
          document.querySelector("#publishDateMin").value = document.querySelector("#publishDateMin").value.replaceAll("/","-");
      })
    }
}





function searchPatient(x) {
    var input, filter, patients, name, i;
    input = document.getElementById("search");
    filter = input.value.toUpperCase();
    patients = document.getElementsByClassName("patient");
    for (i = 0; i < patients.length; i++) {
      switch(x){
        case "patient-name": 
          name = patients[i].getElementsByTagName("td")[0].getElementsByTagName("a")[0];
          break;
        case "date_of_admission":
          name = patients[i].getElementsByTagName("td")[1];
          break;
        case "docter_name":
          name = patients[i].getElementsByTagName("td")[2];
          break;
      }
      if (name.innerHTML.toUpperCase().indexOf(filter) > -1) {
        patients[i].style.display = "";
      } else {
        patients[i].style.display = "none";
      }
    }
}

function filterPatient() {
  var filter = document.getElementsByName('filter');

    for(i = 0; i < filter.length; i++) {
      if(filter[i].checked)
        searchPatient(filter[i].value)
    }
}

function searchDate(){
    filterPatient() 
    var minDate, maxDate, date;

    minDate = new Date(document.querySelector("#min").value)
    maxDate = new Date(document.querySelector("#max").value)

    patients = document.getElementsByClassName("patient");
    for (i = 0; i < patients.length; i++) {
      date = new Date(patients[i].getElementsByTagName("td")[1]);
      if (date.getTime() > minDate.getTime() && date.getTime() < maxDate.getTime() ) {
        patients[i].style.display = "";
      } else {
        patients[i].style.display = "none";
      }
    }
}
