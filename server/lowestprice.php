<?php
// required headers
header("Content-Type:application/json");

include_once ('db.php');
include('response_protocol.php')

if(!empty($_GET['name']))
{
  $name=$_GET['name'];
  $sqlstatement="SELECT name, price, itemid, providerid FROM items WHERE name LIKE '".$name."'ORDER BY price ;";
  $result = $mysqli->query($sqlstatement);
  $row = mysqli_fetch_assoc($result);
  $price = $row['price'];
  $itemid = $row['itemid'];
  $providerid = $row['providerid'];

  //Find name of provider
  $sqlstatement1="SELECT provider FROM providers WHERE providerid =".$providerid.";";
  $providernameresult = $mysqli->query($sqlstatement1);
  $providername = mysqli_fetch_assoc($providernameresult);
  $provider = $providername['provider'];

  //create response json
  $response = array();
  $response["name"] = $name;
  $response["price"] = $price;
  $response["provider"] = $provider;
  
  if(empty($response))
  {
    response(200,"Product Not Found",NULL);
  }
  else
  {
    response(200,"Product Found",$response);
  }
  
}
else
{
  response(400,"Invalid Request",NULL);
}

?>