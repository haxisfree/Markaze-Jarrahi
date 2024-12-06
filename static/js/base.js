function documentLoad(){
  var table, numberOfRows, row;
  table = document.querySelector("table");
  if(table){
      numberOfRows = table.querySelector("tbody").children.length;
      if(numberOfRows <= 1){  
          table.querySelector(".empty-table").style.display="table-row";
      }
      else{
          table.querySelector(".empty-table").style.display="none";
      }
  }
}

function goBack(){
    var value = document.referrer.match(/edit/) || document.referrer.match(/discount/);
    if(value){
        history.go(-3);
    }
    else{
        history.go(-1);
    }
}
