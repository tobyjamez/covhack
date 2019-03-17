<?php
// required headers
header("Content-Type:application/json");

include_once ('db.php');

if(!empty($_POST['name']))
{
  $name=$_POST['name'];
  $sqlstatement="SELECT name, price, itemid, providerid FROM items WHERE name LIKE '".$name."'ORDER BY price ;";
  $result = $mysqli->query($sqlstatement);
  $row = mysqli_fetch_assoc($result);

  $itemid = $row['itemid'];

  //look in account number 1 for list of object ids
  $sqlstatement1="INSERT INTO basket VALUES (1,".$itemid.");";
  //return array of object ids
  $result = $mysqli->query($sqlstatement1);

  if(empty($result))
  {
    response(200,"Product Not Found",NULL);
  }
  else
  {
    response(200,"Product Found","Item inserted");
  }
  
}
else
{
  response(400,"Invalid Request",NULL);
}

function response($status,$status_message,$data)
{
  header("HTTP/1.1 ".$status);
  
  $response['status']=$status;
  $response['status_message']=$status_message;
  $response['data']=$data;
  
  $json_response = json_encode($response);
  echo $json_response;
}

?>