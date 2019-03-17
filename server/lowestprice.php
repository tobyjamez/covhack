<?php
// required headers
header("Access-Control-Allow-Origin: *");
header("Content-Type: application/json; charset=UTF-8");
header("Access-Control-Allow-Methods: POST");
header("Access-Control-Max-Age: 3600");
header("Access-Control-Allow-Headers: Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With");

include_once ('db.php');
$data = json_decode(file_get_contents("php://input"));
if(!empty($data->name)){

  $sqlstatement="SELECT name, price, itemid, providerid FROM items WHERE name LIKE '".$data->name."'ORDER BY price ;";
  $result = $mysqli->query($sqlstatement);

  //Get relevant data about item
  $row = mysqli_fetch_assoc($result);
  if($row!=0){
    $price = $row['price'];
    $itemid = $row['itemid'];
    $providerid = $row['providerid'];

    //Find name of provider
    $sqlstatement1="SELECT provider FROM providers WHERE providerid =".$providerid.";";
    $providernameresult = $mysqli->query($sqlstatement1);
    $providername = mysqli_fetch_assoc($providernameresult);
    $provider = $providername['provider'];
    echo $provider;

    //create response json
    $response = array();
    $response["name"] = $name;
    $response["price"] = $price;
    $response["provider"] = $provider;
    $jsonDataEncoded = json_encode($response);

    // set response code - 201 created
    http_response_code(201);

    // tell the user
    echo $jsonDataEncoded
  }
  else{
    // set response code - 503 service unavailable
    http_response_code(503);

    // tell the user
    echo json_encode(array("message" => "Unable to find item."));
  }
}
else{
 
    // set response code - 400 bad request
    http_response_code(400);
 
    // tell the user
    echo json_encode(array("message" => "Data is incomplete, please enter an item name."));
}
?>