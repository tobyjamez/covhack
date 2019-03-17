<?php
// required headers
header("Content-Type:application/json");

include_once ('db.php');

if(!empty($_GET['name']))
{
  $sqlstatement="SELECT name, price, itemid, providerid FROM items WHERE name LIKE '".$_GET['name']."'ORDER BY price ;";
  $result = $mysqli->query($sqlstatement);

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
  $jsonDataEncoded = json_encode($response);


  $price = $price;
  
  if(empty($price))
  {
    response(200,"Product Not Found",NULL);
  }
  else
  {
    response(200,"Product Found",$price);
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